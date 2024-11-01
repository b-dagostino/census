from importlib.machinery import ModuleSpec, SourceFileLoader
from types import ModuleType

from census.interface import DatasetClass


class CensusModule(ModuleType):
    _DATASET_MAPPING: dict[int | None, type[DatasetClass]]

    def __call__(self) -> type[DatasetClass]:
        return self._DATASET_MAPPING[None]

    def __getitem__(self, key: int | None) -> type[DatasetClass]:
        return self._DATASET_MAPPING[key]


class CensusProductLoader(SourceFileLoader):
    def create_module(self, spec: ModuleSpec) -> ModuleType | None:
        return CensusModule(spec.name)
