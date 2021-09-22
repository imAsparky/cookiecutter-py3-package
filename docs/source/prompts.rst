.. include:: /extras.rst.txt

=======
Prompts
=======

*Copyright 2015, Audrey Roy Greenfeld*

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
~~~~~~~~~
Your full name.

email
~~~~~
Your email address.

github_username
~~~~~~~~~~~~~~~
Your GitHub username.

project_name
~~~~~~~~~~~~
The name of your new Python package project. This is used in documentation,
so spaces and any characters are fine here.

git_project_name
~~~~~~~~~~~~~~~~
The name of the GitHub project repository you have created.

If it is the same as your project_name but with hyphens instead of spaces leave
this blank.  Your GitHub repository name will be generated with hyphens.

If its different enter your project GitHub repository name here.

project_slug
~~~~~~~~~~~~
The namespace of your Python package. This should be Python import-friendly.
Typically, it is the slugified version of project_name. Note: your PyPi
project will use project_slug, so change those in the
README afterwards.

project_short_description
~~~~~~~~~~~~~~~~~~~~~~~~~
A 1-sentence description of what your Python package does.

pypi_username
~~~~~~~~~~~~~
Your Python Package Index account username.

version
~~~~~~~
The starting version number of the package.


Options
-------

The following package configuration options set up different features for your
project.

**add_pyup_badge**
  *default = n*

  Whether to include a `pyup <https://github.com/pyupio/pyup>`_ badge.

**command_line_interface**
  *default = Click*

  Whether to create a console script using Click. Console script entry point
  will match the project_slug.
  Options: ['Click', 'Argparse', 'No command-line interface']

**create_author_file**
   *default = y*

   Whether to create an authors file.

**create_conventional_commits_edit_message**
   *default = y*

   Whether to use a commit message that helps you adhere to the
   `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_
   specification.

   If you plan to use the create_auto_CHANGELOG feature, this template will
   help you keep your messages in the correct format for the auto CHANGELOG
   feature.

.. important::

    If you choose yes, don't forget to run the following command after
    initiating git to let git know you are using a custom template.

    .. code-block:: bash

        git config --local commit.template .github/.git-commit-template.txt

**create_repo_auto_test_workflow**
  *default = y*

  A GitHub action workflow will run your test suite using tox and pytest
  when creating a pull request to the main branch.

.. todo::

    Create a tutorial to demonstrate GitHub protected branches configuration
    to make the best use of the create_repo_auto_test_workflow feature.

    See `Issue 72 <https://github.com/imAsparky/cookiecutter-py3-package/issues/72>`_.


**create_auto_CHANGELOG**
  *default = y*

  create_auto_CHANGELOG will use GitHub actions to generate a changelog using
  a cron job, scheduled daily.

**github_CHANGELOG_access_token**
  *default = secrets.GITHUB_TOKEN*

  For new or small repositories, select `secrets.GITHUB_TOKEN`.
  This is adequate for most small packages.

  For larger repositories, the `GITHUB_TOKEN` may error on the rate limit when
  generating the CHANGELOG.   If so you will need a PAT so
  select `secrets.CHANGELOG_UPDATE`.

  After generating your GitHub PAT, ensure you use `CHANGELOG_UPDATE` as the
  repository secret name.  Be careful not to share the secret or commit it to
  the repository accidentally.

  See `Encrypted Secrets <https://docs.github.com/en/actions/reference/encrypted-secrets>`_
  for more information on generating secrets and repository security.

**use_GH_action_semantic-version**
  *default = y*

  A GitHub action workflow will check your git commit message's information,
  update the semantic version, and publish assets to your package repository.

  A GitHub PAT is required, and the repository secret is named `SEM_VER`
  for this feature to work.

**use_GH_custom_issue_templates**
  *default = y*

  Four custom GitHub issue templates for your package:

  #. bug-report.md
  #. chore.md
  #. documentation-request.md
  #. feature-request.md

  The custom issue templates prompt users to help provide enough information
  in a templated format.

  The default assignee is you; however, re-assign if required at creation
  time or any time after.

  See the critical template markdown file settings below for a feature request.

.. code-block:: yaml

    ---
    name: Feature request
    about: Suggest an idea for this project
    title: "[FEAT]:"
    labels: enhancement
    assignees: { { cookiecutter.github_username } }
    ---

| If you prefer, a simple issue template is available for use with all
  issues if you choose `no` for this feature.

**automatic_set_up_git_and_initial_commit**
   *default = y*

   pre-requisites:

   #. git_project_name
   #. github_username
   #. email

   Initiation of your local git repository is automatic; all files are added
   and committed with a conventional commits style message.

   You can run a git reflog and check all is ok before pushing to the
   repository.

.. code-block:: bash

    git reflog

.. note::

  Selecting this option also includes automatically adding the conventional
  commits message template to git config if you have chosen that option.


**open_source_license**
    *default = MIT*

    Choose a `license <https://choosealicense.com/>`_. Options:

    1. MIT License,
    2. BSD license,
    3. ISC license,
    4. Apache Software License 2.0,
    5. GNU General Public License v3,
    6. Not open source
