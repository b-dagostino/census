from __future__ import annotations

from collections import deque
from collections.abc import (
    Hashable,
    ItemsView,
    KeysView,
    ValuesView,
)
from types import MappingProxyType, SimpleNamespace
from typing import Any, Self

from census.api.models import Dataset, ProjectOpenDataCatalog
from census.utils import get_json_from_url


class CensusNamespace(SimpleNamespace):
    NO_VINTAGE_KEY = None

    def __init__(self, name: str | None = None, **kwargs: Any) -> None:
        self._datasets: dict[Hashable, Dataset] = {}
        self._name: str | None = name
        self._namespaces: set[str] = set()

    @property
    def datasets(self) -> MappingProxyType[Hashable, Dataset]:
        return MappingProxyType(self._datasets)

    @property
    def name(self) -> str | None:
        return self._name

    @property
    def namespaces(self) -> set[str]:
        return self._namespaces

    def items(self) -> ItemsView[Hashable, Dataset]:
        return MappingProxyType(self._datasets).items()

    def keys(self) -> KeysView[Hashable]:
        return MappingProxyType(self._datasets).keys()

    def values(self) -> ValuesView[Dataset]:
        return MappingProxyType(self._datasets).values()

    def __call__(self) -> Dataset:
        return self._datasets[self.NO_VINTAGE_KEY]

    def __getitem__(self, key) -> Dataset:
        return self._datasets[key]

    def __iter__(self):
        return iter(MappingProxyType(self._datasets))

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self._name}', {tuple(sorted(self.namespaces))}, {tuple(self.keys())})"

    @classmethod
    def from_catalog(cls: type[Self], catalog: ProjectOpenDataCatalog) -> Self:
        """
        Create namespace from (validated) API catalog.
        """

        def add_dataset(namespace: Self, dataset: Dataset):
            dataset_namespace_path = deque(dataset.c_dataset)

            while dataset_namespace_path:
                namespace_head = dataset_namespace_path.popleft()
                if not hasattr(namespace, namespace_head):
                    setattr(namespace, namespace_head, cls(namespace_head))
                    namespace._namespaces.add(namespace_head)
                namespace = getattr(namespace, namespace_head)

            assert isinstance(namespace, cls)
            if dataset.c_vintage is not None:
                assert dataset.c_vintage not in namespace._datasets
                namespace._datasets[dataset.c_vintage] = dataset
            else:
                assert None not in namespace._datasets
                namespace._datasets[cls.NO_VINTAGE_KEY] = dataset

        namespace = cls()
        for dataset in sorted(
            catalog.dataset,
            key=lambda x: x.c_vintage if x.c_vintage is not None else float("inf"),
        ):
            add_dataset(namespace, dataset)

        return namespace

    @classmethod
    def from_url(cls: type[Self], url: str) -> Self:
        return cls.from_catalog(ProjectOpenDataCatalog(**get_json_from_url(url)))
