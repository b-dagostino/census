from typing import ClassVar as _ClassVar

# from census.api.models import Variable as _Variable
from census.interface import GeographyEnum as _GeographyEnum, VariablesEnum as _VariablesEnum, Variable as _Variable

from {{ dataset_baseclass_module }} import {{ dataset_baseclass_name }} as _{{ dataset_baseclass_name }}
{% set class_name, dataset_class = dataset_class %}
class {{ class_name }}(_{{ dataset_baseclass_name }}):
    """
    {{ dataset_class.title }}

    {{ dataset_class.description }}
    """
    _title: _ClassVar[str] = '''{{ dataset_class.title }}'''
    _description: _ClassVar[str] = '''{{ dataset_class.description }}'''
    _vintage: _ClassVar[int | None] = {{ dataset_class.vintage }}
    _api_endpoint: _ClassVar[str] = '{{ dataset_class.api_endpoint }}'
    {% if dataset_class.geography is defined %}
    class Geography(_GeographyEnum):
        {%- if dataset_class.geography is not none %}
        {%- for k, v in dataset_class.geography | dictsort %}
        {{ k }}: tuple[str] = ('''{{ v }}''', )
        """{{ v }}"""
        {%- endfor %}
        {%- endif %}
    {% endif %}
    {% if dataset_class.variables is defined %}
    class Variables(_VariablesEnum):
        {%- for variable_id, (k, variable) in dataset_class.variables | dictsort %}
        {{ variable_id }}: tuple[str, _Variable] = ('''{{ k }}''', _Variable('''{{ k }}''', {{ None if variable.concept is none else "'''{}'''".format(variable.concept) }}, '''{{ variable.label }}''', {% if variable.values.item is defined and variable.values.item is not none %}({% for k, v in variable.values.item.items() %}('''{{ k }}''', '''{{ v }}'''),{% endfor %}){% else %}None{% endif %}))
        '''{{ variable.label }}'''
        {%- endfor %}
    {% endif %}