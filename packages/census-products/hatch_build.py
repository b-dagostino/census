from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class BuildCensusProducts(BuildHookInterface):
    PLUGIN_NAME = "build_census_products"

    def _generate_census_products(self):
        import asyncio
        from pathlib import Path

        from census.api.models import ProjectOpenDataCatalog
        from census.api.urls import API_DATA_CATALOG, API_DATA_CATALOG_2022
        from census.generator.package_builder import CensusPackageBuilder

        catalog = ProjectOpenDataCatalog.from_url(API_DATA_CATALOG_2022)
        asyncio.run(catalog.get_dataset_variables_and_geography())
        cb = CensusPackageBuilder.from_catalog(catalog, )
        cb.build_package(Path(self.root) / "src" / "census",  delete_existing=True)

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        if self.target_name == "sdist":
            print("Generating census products...")
            self._generate_census_products()

        # return super().initialize(version, build_data)
