{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.git_project_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.git_project_name }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.git_project_name }}/badge/?version=latest
        :target: https://{{ cookiecutter.git_project_name }}.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.git_project_name }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.git_project_name }}/
     :alt: Updates
{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.git_project_name }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
-------
