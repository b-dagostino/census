from pathlib import Path
from typing import Self

from attrs import define, field
from jinja2 import Environment, PackageLoader

import census.interface
from census.api.models import ProjectOpenDataCatalog
from census.generator.namespace import CensusNamespace
from census.utils import RecursiveDefaultDict, make_identifer

_INIT_TEMPLATE = "__init__.py"
_DATASET_CLASSES_TEMPLATE = "dataset_class.py"
_DATASET_BASECLASS_MODULE = census.interface.__name__
_DATASET_BASECLASS_NAME = census.interface.DatasetClass.__name__

_jenv = Environment(loader=PackageLoader(__name__))


@define
class CensusPackageBuilder:
    _census_namespace: CensusNamespace = field(repr=False)
    _package_name: str = "products"

    _template_context: dict = field(
        repr=False, init=False, factory=RecursiveDefaultDict
    )

    @staticmethod
    def _prepare_directory(path: Path, delete_existing: bool = False):
        import shutil

        if path.exists() and delete_existing:
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)

    def _create_census_namespace_package(
        self,
        census_namespace: CensusNamespace,
        root_dir: Path,
        is_package_root: bool = False,
    ) -> None:
        root_dir.mkdir(parents=True, exist_ok=True)
        self._template_context["is_package_root"] = is_package_root
        self._template_context["dataclass_module"] = Path(
            _DATASET_CLASSES_TEMPLATE
        ).stem
        self._template_context["dataset_baseclass_module"] = _DATASET_BASECLASS_MODULE
        self._template_context["dataset_baseclass_name"] = _DATASET_BASECLASS_NAME

        def make_dataset_classes():
            if not census_namespace.datasets:
                if "dataset_classes" in self._template_context:
                    del self._template_context["dataset_classes"]
                return

            dataset_classes = RecursiveDefaultDict()
            for vintage, dataset in census_namespace.datasets.items():
                class_name = (
                    "".join(map(str.capitalize, dataset.c_dataset))
                    + f"_{dataset.c_vintage}"
                )
                dataset_classes[class_name]["title"] = dataset.title
                dataset_classes[class_name]["description"] = dataset.description
                dataset_classes[class_name]["vintage"] = vintage
                dataset_classes[class_name]["api_endpoint"] = dataset.distribution[
                    0
                ].accessURL

                for i, (k, variable) in enumerate(dataset.variables.variables.items()):
                    concept = make_identifer(variable.concept) if variable.concept else str(variable.concept)
                    variable_id = f"{concept}_{make_identifer(variable.label)}"
                    if variable_id in dataset_classes[class_name]["variables"]:
                        # print(f'{variable_id!r} in dataset_classes[{class_name!r}]["variables"]')
                        variable_id = variable_id + f"_{i}"
                    assert variable_id not in dataset_classes[class_name]["variables"]
                    dataset_classes[class_name]["variables"][variable_id] = (k, variable)     

                dataset_classes[class_name]["geography"] = (
                    None
                    if dataset.geography.fips is None
                    else {
                        make_identifer(fips.name): fips.name
                        for fips in dataset.geography.fips
                    }
                )

                self._template_context["dataset_class"] = (
                    class_name,
                    dataset_classes[class_name],
                )
                template = _jenv.get_template(_DATASET_CLASSES_TEMPLATE)
                output = template.render(self._template_context)
                dataset_class_file = root_dir / f"_{class_name}.py"
                dataset_class_file.write_text(output, encoding="utf-8")

            self._template_context["dataset_classes"] = dataset_classes

        def make_init_file():
            init_file = root_dir / _INIT_TEMPLATE
            template = _jenv.get_template(_INIT_TEMPLATE)
            init_file.write_text(
                template.render(self._template_context), encoding="utf-8"
            )

        make_dataset_classes()
        make_init_file()

        # Recurse for namespaces
        for namespace in census_namespace.namespaces:
            self._create_census_namespace_package(
                getattr(census_namespace, namespace),
                root_dir=root_dir / namespace,
            )

    def build_package(
        self,
        root_dir: str | Path = Path.cwd(),
        delete_existing: bool = False,
    ) -> None:
        package_dir: Path = Path(root_dir) / self._package_name
        self._template_context["package_name"] = self._package_name
        self._template_context["package_dir"] = package_dir

        # Setup package
        self._prepare_directory(package_dir, delete_existing=delete_existing)

        self._create_census_namespace_package(
            self._census_namespace, package_dir, is_package_root=True
        )

    @classmethod
    def from_catalog(
        cls: type[Self], catalog: ProjectOpenDataCatalog, **kwargs
    ) -> Self:
        census_namespace = CensusNamespace.from_catalog(catalog)

        return cls(census_namespace=census_namespace, **kwargs)

    @classmethod
    def from_catalog_url(cls: type[Self], url: str, **kwargs) -> Self:
        census_namespace = CensusNamespace.from_url(url)

        return cls(census_namespace=census_namespace, **kwargs)
