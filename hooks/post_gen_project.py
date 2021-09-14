#!/usr/bin/env python
"""cookiecutter-py3-package post package generation jobs."""
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """Remove files not required for this generated python package."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "{{ cookiecutter.create_conventional_commits_edit_message }}" != "y":
        remove_file(".github/.git-commit-template.txt")

    if "{{ cookiecutter.create_auto_CHANGELOG }}" != "y":
        remove_file("CHANGELOG.md")
        remove_file(".github/workflows/update-changelog.yaml")

    if "{{ cookiecutter.create_auto_CHANGELOG }}" == "y":
        remove_file("HISTORY.rst")

    if "{{ cookiecutter.create_repo_auto_test_workflow }}" != "y":
        remove_file(".github/workflows/test_contribution.yaml")

    if "{{ cookiecutter.use_GH_action_semantic_version }}" != "y":
        remove_file(".github/workflows/semantic_release.yaml")
        remove_file(".github/semantic.yaml")
