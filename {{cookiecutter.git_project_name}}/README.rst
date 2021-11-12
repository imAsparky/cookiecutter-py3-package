{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{%- if cookiecutter.use_repo_status_badge != "n" %}
.. image:: https://www.repostatus.org/badges/latest/{{cookiecutter.use_repo_status_badge}}.svg
   :target: https://www.repostatus.org/#{{cookiecutter.use_repo_status_badge}}
   :alt: Project Status: {{cookiecutter.use_repo_status_badge}}
{%- endif %}

{%- if cookiecutter.add_pyup_badge == "y" %}
.. image:: https://pyup.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.git_project_name}}/shield.svg
   :target: https://pyup.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.git_project_name}}/
   :alt: Updates
{%- endif %}



{{ cookiecutter.project_short_description }}


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `imAsparky/cookiecutter-py3-package`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`imAsparky/cookiecutter-py3-package`: https://github.com/imAsparky/cookiecutter-py3-package
