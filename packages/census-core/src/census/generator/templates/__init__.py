{%- if is_package_root is true -%}
def _install_module_importer():
    import sys
    from importlib import invalidate_caches
    from importlib.machinery import FileFinder
    from pathlib import Path

    from census.importer import CensusProductLoader

    census_products_path = Path(__file__).parent.resolve()

    def census_product_path_hook(path: str):
        resolved_path = Path(path).resolve()
        if resolved_path == census_products_path or resolved_path.is_relative_to(
            census_products_path
        ):
            return FileFinder(path, (CensusProductLoader, [".py"]))
        raise ImportError

    sys.path_hooks.insert(0, census_product_path_hook)
    sys.path_importer_cache.clear()
    invalidate_caches()


_install_module_importer()
del _install_module_importer
{%- endif -%}
{%- if dataset_classes is defined -%}
{%- for class_name, dataset_class in dataset_classes.items() %}
from ._{{ class_name }} import {{ class_name }}
{%- endfor %}

_DATASET_MAPPING = {
    {%- for class_name, dataset_class in dataset_classes.items() %}
    {{ dataset_class.vintage }} : {{ class_name }},
    {%- endfor %}
}

__all__ = [
{%- for class_name in dataset_classes.keys() %}
    "{{ class_name }}",
{%- endfor %}
]

def __dir__():
    return __all__
{%- endif -%}