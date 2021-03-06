.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: how-to-quickstart ; Index

.. _how-to-quickstart:
==========
Quickstart
==========

See :ref:`Reference Project Inputs<project-inputs>` for all information
collected to create a new cookiecutter-py3-package.

Create a GitHub Repository
--------------------------

Your new GitHub repository information is required to generate
your cookiecutter-py3-package in these steps.

project_name
~~~~~~~~~~~~

The name of your new cookiecutter-py3-package,  used in the documentation,
so spaces and any characters are acceptable here.

Typically the repository name in sentence form.

project_short_description
~~~~~~~~~~~~~~~~~~~~~~~~~

A  sentence describes your cookiecutter-py3-package.

Typically the repository description.


Create Virtual Environment
--------------------------

**Select the tab for your preferred Operating System.**

.. tab:: Linux

    .. code-block:: bash
        :caption: **bash/zsh**

        python3 -m venv venv
        source venv/bin/acivate
        pip install --upgrade pip

    You will have a folder structure similar to this.

    .. code-block:: bash

            packages
            └── venv


.. tab:: macOS


    .. code-block:: bash
        :caption: **bash/zsh**

        python3 -m venv venv
        source venv/bin/acivate
        pip install --upgrade pip

    You will have a folder structure similar to this.

    .. code-block:: bash

            packages
            └── venv

.. tab:: Windows

    If you have installed Python in your PATH and PATHEXT.

    .. code-block:: bash
        :caption: **cmd/PowerShell**

        python3 -m venv venv

        C:\> venv\Scripts\activate.bat  # cmd.exe
        PS C:\> venv\Scripts\Activate.ps1 # Powershell

        pip install --upgrade pip

    Otherwise use

    .. code-block:: bash
        :caption: **cmd/PowerShell**

        c:\>c:\Python36\python -m venv c:\path\to\packages\my_env
        PS C:\> <venv>\Scripts\Activate.ps1

        C:\> venv\Scripts\activate.bat  # cmd.exe
        PS C:\> venv\Scripts\Activate.ps1 # Powershell

        pip install --upgrade pip

    You will have a folder structure similar to this.

    .. code-block:: bash

            packages
            └── venv

.. _quick_install-cookiecutter:
Install Cookiecutter
--------------------

Firstly it's advisable to upgrade pip using the following command.

.. code-block:: bash
    :caption: **Linux, macOS and Windows**

    pip install --upgrade pip

You will see something like this in your CLI.

.. code-block:: cmd

    Requirement already satisfied: pip in ./my_env/lib/python3.9/site-packages (21.2.3)
    Collecting pip
     Using cached pip-21.2.4-py3-none-any.whl (1.6 MB)
    Installing collected packages: pip
      Attempting uninstall: pip
        Found existing installation: pip 21.2.3
        Uninstalling pip-21.2.3:
          Successfully uninstalled pip-21.2.3
    Successfully installed pip-21.2.4

Install cookiecutter_ into your virtual environment.

.. code-block:: bash
    :caption: **Linux, macOS and Windows**

    pip install cookiecutter

Start Cookiecutter-Py3-Package
------------------------------

In your packages folder, use the following command.

.. code-block:: bash
    :caption: **Linux, macOS and Windows**

    cookiecutter https://github.com/imAsparky/cookiecutter-py3-package

Cookiecutter will ask questions to set your package up.
If you're unsure or don't know what to enter, stick with the defaults.

See :ref:`Reference-Inputs<project-inputs>` for more details about the
cookiecutter-py3- project options.

.. code-block:: bash

    packages
        ├── venv
        └── my-new-package


Install Dependencies
--------------------


Change into your project directory.


.. code-block:: bash

    cd <your my-new-package folder>


Install dependencies.

.. code-block:: bash

    pip install -r requirements_dev.txt


Congratulations, you have created your new Python Package.

Depending on your chosen options, there are several ways to proceed with
pushing to GitHub.  If you are unsure, see our
:ref:`git push tutorial<create-first-git-push>` for more information.



.. _cookiecutter: https://cookiecutter.readthedocs.io/en/1.7.2/README.html
