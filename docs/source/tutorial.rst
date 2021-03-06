========
Tutorial
========

*Copyright 2015, Audrey Roy Greenfeld*

.. note:: Did you find any of these instructions confusing? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://github.com/imAsparky/cookiecutter-py3-package/blob/main/docs/tutorial.rst

To start with, you will need a `GitHub account`_ and an account on `PyPI`_.
Create these before you get started on this tutorial. If you are new to Git and
GitHub, you should probably spend a few minutes on some of the tutorials at the
top of the page at `GitHub Help`_.

.. _`GitHub account`: https://github.com/
.. _`GitHub Help`: https://help.github.com/

Step 1: Create a GitHub Repo
----------------------------

We do this step first to make sure that your new package name is available.

Your GitHub package name can use a hyphen -, however, the module name must use
an underscore _.

Don't worry; we have your back; go right ahead if you would like to use hyphens
in your package name.  We generate your module names correctly using
underscores from the information gathered when you cookiecutter your new
project.

.. todo::

    #. Fix the git repo bash commands in Step 1 of the tutorial.
    #. The git bash commands may be better lower down the list as well.

    See `Issue 69 <https://github.com/imAsparky/cookiecutter-py3-package/issues/69>`_.

.. code-block:: bash

    cd mypackage
    git init .
    git add .
    git config --local commit.template .github/.git-commit-template.txt
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:myusername/mypackage.git
    git push -u origin main

Where ``myusername`` and ``mypackage`` are adjusted for your username and
package name.

You will need an ssh key to push local changes to your repository.

You can `Generate`_ a new key or `Add`_ an existing one.

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/


Step 2: Install Cookiecutter
----------------------------

First, you need to create and activate a virtualenv for the package project.
Use your favourite method, or create a virtualenv for your new package
like this:

.. code-block:: bash

    virtualenv ~/.virtualenvs/mypackage

Here, ``mypackage`` is the name of the package that you'll create.

Activate your environment:

.. code-block:: bash

    source bin/activate

or use the . source shortcut like this

.. code-block:: bash

    . bin/activate

On Windows, activate it like this. You may find that using a Command Prompt
Terminal works better than gitbash.

.. code-block:: powershell

    > \path\to\env\Scripts\activate


Install cookiecutter:

.. code-block:: bash

    pip install cookiecutter


Step 3 : Generate Your Package
------------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it to the cookiecutter-py3-package repository:

.. code-block:: bash

    cookiecutter https://github.com/imAsparky/cookiecutter-py3-package.git

Cookiecutter will ask questions to set your package up.
If you're unsure or don't know what to enter, stick with the defaults.



Step 4: Install Dev Requirements
--------------------------------

You should still be in the root folder, the one containing the
``requirements_dev.txt`` file.

Check your virtualenv is still activated. If it isn't, activate it now.
Install the new project's local development requirements:

.. code-block:: bash

    pip install -r requirements_dev.txt


Step 5: Set Up Read the Docs
----------------------------

`Read the Docs`_ hosts documentation for the open-source community. Think of it
as Continuous Documentation.

Log into your account at `Read the Docs`_ . If you don't have one, create one
and log into it.

If you are not at your dashboard, choose the pull-down next to your username in
the upper right, and select "My Projects". Choose the button to Import the
repository and follow the directions.

Now your documentation will get rebuilt when you make documentation changes to
your package.


.. _`Read the Docs`: https://readthedocs.org/

Step 6: Set Up pyup.io
----------------------

`pyup.io`_ is a service that helps you to keep your requirements files up to
date. It sends you automated pull requests whenever there's a new release for
one of your dependencies.

To use it, create a new account at `pyup.io`_ or log into your existing account.

Click on the green ``Add Repo`` button in the top left corner and select the
repo you created in Step 3. A popup will ask you whether you want to pin your
dependencies. Click on ``Pin`` to add the repo.

When your repository is correctly set up, the pyup.io badge will show your current
update status.


.. _`pyup.io`: https://pyup.io/


.. todo::

    Add a tutorial to describe using Test Pypi.

    See `Issue 13 <https://github.com/imAsparky/cookiecutter-py3-package/issues/13>`_.

Step 7: Release on PyPI
-----------------------

The Python Package Index or `PyPI`_ is the official third-party software
repository for the Python programming language. Python developers intend it to
be a comprehensive catalog of all open source Python packages.

When you are ready, release your package the standard Python way.

See `PyPI Help`_ for more information about submitting a package.

Here's a release checklist you can use:
https://github.com/imAsparky/cookiecutter-py3-package/blob/main/docs/source/pypi_release_checklist.rst

.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: https://pypi.org/help/#publishing


Having problems?
----------------

Visit our :ref:`troubleshooting` page for help. If that doesn't help, go to our
`Issues`_ page and create a new Issue. Be sure to give as much information as possible.

.. _`Issues`: https://github.com/imAsparky/cookiecutter-py3-package/issues
