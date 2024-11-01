from enum import Enum
from typing import Any, ClassVar, Self, NamedTuple, Sequence

import pandas as pd
from aenum import MultiValueEnum
from attrs import define, field


class Variable(NamedTuple):
    name: str
    concept: str | None
    label: str
    value_map: dict | None


class VariablesEnum(MultiValueEnum): ...


class GeographyEnum(MultiValueEnum): ...


class DatasetMetaClass(type):
    _title: str
    _description: str
    _vintage: int | None
    _api_endpoint: str

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def vintage(self) -> int | None:
        return self._vintage

    @property
    def api_endpoint(self) -> str:
        return self._api_endpoint


class DatasetClass(metaclass=DatasetMetaClass):
    Variables: ClassVar[type[VariablesEnum]]
    Geography: ClassVar[type[GeographyEnum]]

    def __new__(cls):
        from census.interface import DatasetQueryBuilder

        return DatasetQueryBuilder(cls)


@define
class DatasetQueryBuilder:
    _dataset: type[DatasetClass]
    _variables: set[str] = field(init=False, factory=set)
    _for: set[tuple[str, str]] = field(init=False, factory=set)
    # _in: set[str] = field(init=False, factory=set)

    @property
    def current_variables(self) -> frozenset[str]:
        return frozenset(self._variables)

    @property
    def current_for_(self) -> frozenset[tuple[str, str]]:
        return frozenset(self._for)

    # @property
    # def current_in_(self) -> frozenset[str]:
    #     return frozenset(self._in)

    def variables(self, *variables: str | Enum) -> Self:
        for variable in variables:
            self._variables.add(self._dataset.Variables(variable).value)
        return self

    def for_(self, *predicates: tuple[str | Enum, Any]) -> Self:
        for k, v in predicates:
            match k:
                case self._dataset.Variables() | self._dataset.Geography():
                    k = str(k.value)

            self._for.add((k, str(v)))
        return self

    def in_(self, *args, **kwargs) -> Self:
        raise NotImplementedError
        return Self

    def _assemble_query(self) -> str:
        query = []

        if self._variables:
            get = f"get={','.join(self._variables)}"
            query.append(get)

        if self._for:
            predicates = ["{}:{}".format(*pred) for pred in self._for]
            for_ = f"for={','.join(predicates)}"
            query.append(for_)

        return (
            self._dataset.api_endpoint + "?" + "&".join(query)
            if query
            else self._dataset.api_endpoint
        )

    def query(self) -> pd.DataFrame:
        from requests import HTTPError, get

        query = self._assemble_query()
        r = get(query)
        try:
            r.raise_for_status()
        except HTTPError as e:
            if r.status_code == 400:
                raise RuntimeError(r.text) from e
            else:
                raise e
        r_json = r.json()
        return pd.DataFrame.from_records(r_json[1:], columns=r_json[0])

    def __call__(
        self,
    ) -> pd.DataFrame:
        return self.query()
