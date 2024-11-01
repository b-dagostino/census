import sys
from pprint import pprint

import pytest
from pydantic import ValidationError

from census.api.models import Geography, ProjectOpenDataCatalog, Variables
from census.api.urls import API_DATA_CATALOG, API_DATA_CATALOG_2022
from census.utils import get_json_from_url


@pytest.fixture
def catalog() -> ProjectOpenDataCatalog:
    return ProjectOpenDataCatalog.from_url(API_DATA_CATALOG)


def test_geography(catalog: ProjectOpenDataCatalog):
    try:
        for i, dataset in enumerate(catalog.dataset):
            geo_url = dataset.c_geographyLink
            geo_json = get_json_from_url(geo_url)
            geo = Geography(**geo_json)
    except ValidationError as e:
        print(f"dataset[{i}]", file=sys.stderr)
        print(geo_url, file=sys.stderr)
        pprint(geo_json, stream=sys.stderr)
        raise e


def test_variables(catalog: ProjectOpenDataCatalog):
    try:
        for i, dataset in enumerate(catalog.dataset):
            vars_url = dataset.c_variablesLink
            vars_json = get_json_from_url(vars_url)
            vars = Variables(**vars_json)
    except ValidationError as e:
        print(f"dataset[{i}]", file=sys.stderr)
        print(vars_url, file=sys.stderr)
        pprint(vars_json, stream=sys.stderr)
        raise e
