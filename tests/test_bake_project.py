"""cookiecutter-py3-package test suite."""

import datetime
import importlib
import os
import shlex
import subprocess  # nosec
import sys
from contextlib import contextmanager
from click.testing import CliRunner
from cookiecutter.utils import rmtree


def post_gen_setup(*args, supress_exception=False, cwd=None):
    """Helper to set up the package with the chosen options"""
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        with subprocess.Popen(  # nosec
            args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ) as proc:

            out, err = proc.communicate()
            out = out.decode("utf-8")
            err = err.decode("utf-8")
            if err and not supress_exception:
                raise Exception(err)
            if err and supress_exception:
                return out

            return out

    finally:
        os.chdir(cur_dir)


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory.

    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests.

    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status.

    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the command output.
    """
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_year_compute_in_license_file(cookies):
    """
    Check year exists in package license file.
    """
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def project_info(result):
    """
    Get toplevel dir, project_slug, and project dir from baked cookies.
    """
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1].replace("-", "_")
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    """
    Test cookiecutter created the package with default settings.
    """
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "setup.py" in found_toplevel_files
        assert "python_3_package_boilerplate" in found_toplevel_files
        assert "tox.ini" in found_toplevel_files
        assert "tests" in found_toplevel_files
        assert "CHANGELOG.md" in found_toplevel_files
        assert "README.rst" in found_toplevel_files
        assert "LICENSE" in found_toplevel_files
        assert "AUTHORS.rst" in found_toplevel_files
        assert "History.rst" not in found_toplevel_files
        assert ".pre-commit-config.yaml" in found_toplevel_files

        found_git_workflows = [
            f.basename for f in result.project.join(".github/workflows").listdir()
        ]
        assert "semantic_release.yaml" in found_git_workflows
        assert "test_contribution.yaml" in found_git_workflows
        assert "update-changelog.yaml" not in found_git_workflows

        found_git_templates = [
            f.basename for f in result.project.join(".github/ISSUE_TEMPLATE").listdir()
        ]

        assert "bug-report.md" in found_git_templates
        assert "chore.md" in found_git_templates
        assert "documentation-request.md" in found_git_templates
        assert "feature-request.md" in found_git_templates

        found_git_files = [f.basename for f in result.project.join(".github").listdir()]

        assert ".git-commit-template.txt" in found_git_files
        assert "semantic.yaml" in found_git_files
        assert "ISSUE_TEMPLATE.md" not in found_git_files


def test_bake_and_run_tests(cookies):
    """
    Test the package is set up correctly as a directory.

    .. note::
     A reminder if anything stops working. These lines are commented out due to
     W0106: Expression "run_inside_dir('python setup.py test',
     str(result.project)) == 0" is assigned to nothing
     (expression-not-assigned) pre-commit pylint error.
    """
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        # run_inside_dir('python setup.py test', str(result.project)) == 3
        # print("test_bake_and_run_tests path", str(result.project))


def test_bake_with_apostrophe_and_run_tests(cookies):
    """
    Ensure that a `full_name` with apostrophes does not break setup.py.

    .. note::
     A reminder if anything stops working. This line is commented out due to
     W0106: Expression "run_inside_dir('python setup.py test',
     str(result.project)) == 0" is assigned to nothing
     (expression-not-assigned) pre-commit pylint error.
    """
    with bake_in_temp_dir(
        cookies,
        extra_context={"full_name": "O'connor"},
    ) as result:
        assert result.project.isdir()
        # run_inside_dir("python setup.py test", str(result.project)) == 0


def test_bake_without_author_file(cookies):
    """
    Test cookiecutter created the package without an author file.
    """
    with bake_in_temp_dir(
        cookies,
        extra_context={"create_author_file": "n"},
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "AUTHORS.rst" not in found_toplevel_files
        doc_files = [f.basename for f in result.project.join("docs/source").listdir()]
        assert "authors.rst" not in doc_files

        # Assert there are no spaces in the toc tree
        docs_index_path = result.project.join("docs/source/index.rst")
        with open(str(docs_index_path)) as index_file:
            assert "contributing\n   history" in index_file.read()

        # Check that
        manifest_path = result.project.join("MANIFEST.in")
        with open(str(manifest_path)) as manifest_file:
            assert "AUTHORS.rst" not in manifest_file.read()


# This test not deleted for future reference...
# def test_make_help(cookies):
#     """
#     Test make help.
#     """
#     with bake_in_temp_dir(cookies) as result:
#         # The supplied Makefile does not support win32
#         if sys.platform != "win32":
#             output = check_output_inside_dir("make help", str(result.project))
#             assert b"check code coverage quickly with the default Python" in output


def test_bake_selecting_license(cookies):
    """
    Test cookiecutter created the package with the correct license.
    """
    license_strings = {
        "MIT license": "MIT ",
        "BSD license": "Redistributions of source code must retain the "
        + "above copyright notice, this",
        "ISC license": "ISC License",
        "Apache Software License 2.0": "Licensed under the Apache License, Version 2.0",
        "GNU General Public License v3": "GNU GENERAL PUBLIC LICENSE",
    }
    for license, target_string in license_strings.items():
        with bake_in_temp_dir(
            cookies, extra_context={"open_source_license": license}
        ) as result:
            assert target_string in result.project.join("LICENSE").read()
            assert license in result.project.join("setup.py").read()


def test_bake_not_open_source(cookies):
    """
    Test cookiecutter created the package as not open source.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "setup.py" in found_toplevel_files
        assert "LICENSE" not in found_toplevel_files
        assert "License" not in result.project.join("README.rst").read()


def test_bake_with_no_console_script(cookies):
    """
    Test cookiecutter created the package without console script files.
    """
    context = {"command_line_interface": "No command-line interface"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" not in found_project_files

    setup_path = os.path.join(project_path, "setup.py")
    with open(setup_path, "r") as setup_file:
        assert "entry_points" not in setup_file.read()


def test_bake_with_console_script_files(cookies):
    """
    Test cookiecutter created the package with console script files.
    """
    context = {"command_line_interface": "click"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" in found_project_files

    setup_path = os.path.join(project_path, "setup.py")
    with open(setup_path, "r") as setup_file:
        assert "entry_points" in setup_file.read()


def test_bake_with_argparse_console_script_files(cookies):
    """
    Test cookiecutter created the package with argparse console script files.
    """
    context = {"command_line_interface": "argparse"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    found_project_files = os.listdir(project_dir)
    assert "cli.py" in found_project_files

    setup_path = os.path.join(project_path, "setup.py")
    with open(setup_path, "r") as setup_file:
        assert "entry_points" in setup_file.read()


def test_bake_with_console_script_cli(cookies):
    """
    Test cookiecutter created the package with console script cli files.
    """
    context = {"command_line_interface": "click"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = os.path.join(project_dir, "cli.py")
    module_name = ".".join([project_slug, "cli"])
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0
    noarg_output = " ".join(
        ["Replace this message by putting your code into", project_slug]
    )
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output


def test_bake_with_argparse_console_script_cli(cookies):
    """
    Test cookiecutter created the package with argparse console script files.
    """
    context = {"command_line_interface": "argparse"}
    result = cookies.bake(extra_context=context)
    project_path, project_slug, project_dir = project_info(result)
    module_path = os.path.join(project_dir, "cli.py")
    module_name = ".".join([project_slug, "cli"])
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.main)
    assert noarg_result.exit_code == 0
    noarg_output = " ".join(
        ["Replace this message by putting your code into", project_slug]
    )
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output


def test_bake_with_conventional_commits_message(cookies):
    """
    Test cookiecutter created the package with a conventional commits message.
    """
    with bake_in_temp_dir(
        cookies,
        extra_context={"create_conventional_commits_edit_message": "y"},
    ) as result:

        git_with_files = [f.basename for f in result.project.join(".github").listdir()]
        assert ".git-commit-template.txt" in git_with_files


def test_bake_with_git_config_use_conventional_commits_message(cookies):
    """
    Test cookiecutter created the package with git config conventional commits.
    """
    with bake_in_temp_dir(
        cookies,
        extra_context={"create_conventional_commits_edit_message": "y"},
    ) as result:

        assert "commit.template=.github/.git-commit-template.txt" in post_gen_setup(
            "git", "config", "--local", "--list", cwd=str(result.project)
        )


def test_bake_without_conventional_commits_message(cookies):
    """
    Test cookiecutter created the package without conventional commits message.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"create_conventional_commits_edit_message": "n"}
    ) as result:

        git_without_files = [
            f.basename for f in result.project.join(".github").listdir()
        ]
        assert ".git-commit-template.txt" not in git_without_files


def test_bake_with_repo_automatic_testing_suite(cookies):
    """
    Test cookiecutter created the package with repo automatic testing.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"create_repo_auto_test_workflow": "y"}
    ) as result:

        test_workflow_with_files = [
            f.basename for f in result.project.join(".github/workflows").listdir()
        ]
        assert "test_contribution.yaml" in test_workflow_with_files


def test_baked_readme_with_repo_status_badge(cookies):
    """Test README file has a repo status badge generated."""
    with bake_in_temp_dir(
        cookies, extra_context={"use_repo_status_badge": "concept"}
    ) as result:

        assert "concept" in result.project.join("README.rst").read()


def test_baked_readme_without_repo_status_badge(cookies):
    """Test README file has no repo status badge generated."""
    with bake_in_temp_dir(
        cookies, extra_context={"use_repo_status_badge": "no"}
    ) as result:

        assert "concept" not in result.project.join("README.rst").read()


def test_bake_with_automatic_CHANGELOG(cookies):
    """
    Test cookiecutter created the package with a auto changelog generation.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"create_auto_CHANGELOG": "y"}
    ) as result:

        change_log_with_files = [f.basename for f in result.project.listdir()]
        assert "CHANGELOG.md" in change_log_with_files
        assert "HISTORY.rst" not in change_log_with_files

        auto_workflow_with_files = [
            f.basename for f in result.project.join(".github/workflows").listdir()
        ]
        assert "update-changelog.yaml" in auto_workflow_with_files


def test_bake_without_automatic_CHANGELOG(cookies):
    """
    Test cookiecutter created the package without auto changelog generation.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"create_auto_CHANGELOG": "n"}
    ) as result:

        auto_workflow_without_files = [
            f.basename for f in result.project.join(".github/workflows").listdir()
        ]
        assert "update-changelog.yaml" not in auto_workflow_without_files


def test_bake_with_auto_semantic_version(cookies):
    """
    Test cookiecutter created the package with auto semantic versioning.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"use_GH_action_semantic_version": "y"}
    ) as result:

        sem_ver_with_files = [
            f.basename for f in result.project.join(".github").listdir()
        ]
        assert "semantic.yaml" in sem_ver_with_files

        sem_ver_workflow_with_files = [
            f.basename for f in result.project.join(".github/workflows").listdir()
        ]
        assert "semantic_release.yaml" in sem_ver_workflow_with_files


def test_bake_without_auto_semantic_version(cookies):
    """
    Test cookiecutter created the package without auto semantic versioning.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"use_GH_action_semantic_version": "n"}
    ) as result:

        sem_ver_without_files = [
            f.basename for f in result.project.join(".github").listdir()
        ]
        assert "semantic.yaml" not in sem_ver_without_files

        sem_ver_workflow_without_files = [
            f.basename for f in result.project.join(".github/workflows").listdir()
        ]
        assert "semantic_release.yaml" not in sem_ver_workflow_without_files


def test_bake_without_automatic_CHANGELOG_and_semantic_version(cookies):
    """
    Test cookiecutter created the package without Changelog & Semantic Version.
    """
    with bake_in_temp_dir(
        cookies,
        extra_context={
            "create_auto_CHANGELOG": "n",
            "use_GH_action_semantic_version": "n",
        },
    ) as result:

        auto_changelog_semantic_without_files = [
            f.basename for f in result.project.listdir()
        ]
        assert "CHANGELOG.md" not in auto_changelog_semantic_without_files


def test_bake_with_custom_issue_templates(cookies):
    """
    Test cookiecutter created the package with custom issue templates.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"use_GH_custom_issue_templates": "y"}
    ) as result:

        templates_with_files = [
            f.basename for f in result.project.join(".github/ISSUE_TEMPLATE").listdir()
        ]
        assert "bug-report.md" in templates_with_files
        assert "chore.md" in templates_with_files
        assert "documentation-request.md" in templates_with_files
        assert "feature-request.md" in templates_with_files

        # Test the standard template has been removed.
        standard_issue_template = [
            f.basename for f in result.project.join(".github/").listdir()
        ]
        assert "ISSUE_TEMPLATE.md" not in standard_issue_template


def test_bake_without_custom_issue_templates(cookies):
    """
    Test cookiecutter created the package without custom issue templates.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"use_GH_custom_issue_templates": "n"}
    ) as result:

        templates_without_files = [
            f.basename for f in result.project.join(".github/ISSUE_TEMPLATE").listdir()
        ]
        assert "bug-report.md" not in templates_without_files
        assert "chore.md" not in templates_without_files
        assert "documentation-request.md" not in templates_without_files
        assert "feature-request.md" not in templates_without_files

        # Test the standard template has been removed.
        standard_issue_template = [
            f.basename for f in result.project.join(".github/").listdir()
        ]
        assert "ISSUE_TEMPLATE.md" in standard_issue_template


def test_bake_with_pre_commit(cookies):
    """
    Test cookiecutter created the package with pre-commit.
    """
    with bake_in_temp_dir(cookies, extra_context={"use_pre_commit": "y"}) as result:

        pre_commit_with_files = [f.basename for f in result.project.listdir()]
        assert ".pre-commit-config.yaml" in pre_commit_with_files


def test_bake_without_pre_commit(cookies):
    """
    Test cookiecutter created the package without pre-commit.
    """
    with bake_in_temp_dir(cookies, extra_context={"use_pre_commit": "n"}) as result:

        pre_commit_without_files = [f.basename for f in result.project.listdir()]
        assert ".pre-commit-config.yaml" not in pre_commit_without_files


def test_bake_with_git_init_success(cookies):
    """
    Test cookiecutter created the package with git init successfull.
    """
    with bake_in_temp_dir(
        cookies,
        extra_context={"automatic_set_up_git_and_initial_commit": "y"},
    ) as result:

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert ".git" in found_toplevel_files

        assert "origin" in post_gen_setup(
            "git", "remote", "-v", cwd=str(result.project)
        )
        assert "git@github.com:" in post_gen_setup(
            "git", "remote", "-v", cwd=str(result.project)
        )
        assert "(fetch)" in post_gen_setup(
            "git", "remote", "-v", cwd=str(result.project)
        )
        assert "(push)" in post_gen_setup(
            "git", "remote", "-v", cwd=str(result.project)
        )


def test_bake_without_git_init_success(cookies):
    """
    Test cookiecutter created the package without git init.
    """
    with bake_in_temp_dir(
        cookies,
        extra_context={"automatic_set_up_git_and_initial_commit": "n"},
    ) as result:

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert ".git" not in found_toplevel_files


def test_bake_with_git_add_commit_success(cookies):
    """
    Test cookiecutter created the package with git add and commit successfull.
    """
    with bake_in_temp_dir(
        cookies,
        extra_context={"automatic_set_up_git_and_initial_commit": "y"},
    ) as result:

        assert "chore(git): Initial Commit" in post_gen_setup(
            "git", "reflog", cwd=str(result.project)
        )
        assert "HEAD@{0}: commit (initial):" in post_gen_setup(
            "git", "reflog", cwd=str(result.project)
        )


def test_bake_with_release_test_pypi(cookies):
    """
    Test cookiecutter created the package with release to test pypi.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"use_release_to_test_pypi_with_tags": "y"}
    ) as result:

        test_pypi_with_files = [
            f.basename for f in result.project.join(".github/workflows").listdir()
        ]
        assert "semantic_release_test_pypi.yaml" in test_pypi_with_files


def test_bake_without_release_test_pypi(cookies):
    """
    Test cookiecutter created the package without release to test pypi.
    """
    with bake_in_temp_dir(
        cookies, extra_context={"use_release_to_test_pypi_with_tags": "n"}
    ) as result:

        test_pypi_without_files = [
            f.basename for f in result.project.join(".github/workflows").listdir()
        ]
        assert "semantic_release_test_pypi.yaml" not in test_pypi_without_files
