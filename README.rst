============================
**Cookiecutter Py3-Package**
============================

|

.. image:: ./docs/source/_static/imgs/logo/logo-cookiecutter-py3-package-1280x640.png
   :alt: cookiecutter-py3-package

|

**A fork of** cookiecutter-pypackage_.

**Currently, this is being updated to meet my specific needs, and perhaps yours.**

**Checkout the** CHANGELOG_ **to see what has been done so far.**

**Checkout the** Projects_ **page to see what is planned.**

**We are aiming for your new package to be an automated Continuous Delivery
workflow experience.**

|

.. image:: https://www.repostatus.org/badges/latest/wip.svg
   :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
   :target: https://www.repostatus.org/#wip

.. image:: https://pyup.io/repos/github/imAsparky/cookiecutter-py3-pacakge/shield.svg
   :target: https://pyup.io/repos/github/imAsparky/cookiecutter-py3-pacakge/

.. image:: http://isitmaintained.com/badge/resolution/imAsparky/cookiecutter-py3-package.svg
   :alt: Project is Maintained
   :target: https://isitmaintained.com/project/imAsparky/cookiecutter-py3-package

.. image:: http://isitmaintained.com/badge/open/imAsparky/cookiecutter-py3-package.svg
   :alt: Project Open Issues
   :target: https://isitmaintained.com/project/imAsparky/cookiecutter-py3-package

.. image:: https://app.codacy.com/project/badge/Grade/4c115acc2b3d4d13b998cdcbdb3cea64
    :target: https://www.codacy.com/gh/imAsparky/cookiecutter-py3-package/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=imAsparky/cookiecutter-py3-package&amp;utm_campaign=Badge_Grade
    :alt: Code Quality

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit


.. image:: https://readthedocs.org/projects/cookiecutter-py3-package/badge/?version=latest
    :target: https://cookiecutter-py3-package.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

A Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/imAsparky/cookiecutter-py3-package/
* Documentation: https://cookiecutter-py3-package.readthedocs.io/
* Free software: BSD license


Features
--------

#. Choose to use a `Conventional-Commits`_ specification custom commits message
   in your built package.
#. An optional GitHub action to automatically update semantic version and
   publish assets to your package repository when a pull request merge is
   closed or manually.
#. Manual semantic versioning and publishing are also available locally,
   bypassing the need for a GitHub action if that is your preferred workflow.
#. An optional GitHub action to generate a package CHANGELOG automatically if
   you choose to version and publish your package manually.
#. An optional GitHub action to run your `Tox`_ package test suite when a
   pull request to the main branch starts.
#. Optional to use to use `pre-commit`_ to identuify simple coding issues
   before submission, with a badge to communicate quickly.
#. `Tox`_ configuration for your package includes an OS and Python test matrix.
   OS includes Linux, macOS and Windows. Python 3.6 - 3.9. (Uses GitHub actions.)
#. An optional suite of custom GitHub issue templates. The four custom issue
   templates prompt users to help provide enough information in a templated
   format for each issue type.
#. Documentation is in the process of being refreshed and organised into the
   `Diataxis`_ documentation framework.
#. `Sphinx`_ docs: Documentation ready for generation with, for example, `Read the Docs`_.
#. Optional to use to use a `Read the Docs`_ badge to communicate quickly.
#. Auto-release to `PyPI`_ when you push a new tag to main (optional). Coming soon.
#. Use commit tags to release to `Test-PyPi`_. Coming soon.
#. An optional Command line interface using Click or Argparse.
#. An option to initialise your local git repository, add files and create the
   first commit automatically. Also if you have opted to use the
   `Conventional-Commits`_ style git commit message template, cookiecutter
   will simultaneously add it to your local git config file.
#. Optional to use to use a `Repo Status`_ badge to communicate quickly.


.. note::

   Initialise your local git requires Git v2.33.0 or above.


Quickstart
----------

See the cookiecutter-py3-package `quickstart`_.

For more details on getting started, see the `cookiecutter-py3-pypackage tutorial`_.

Contributing
------------

Contributions are very welcome and appreciated!

You can contribute in many ways.

See `How-To Contribute
<https://cookiecutter-py3-package.readthedocs.io/en/latest/how-tos/
how-to-contribute.html>`_ to help you get started.

Please take a moment to read our `Code of Conduct
<https://cookiecutter-py3-package.readthedocs.io/en/latest/
code-of-conduct.html#code-of-conduct>`_.


Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `ardydedase/cookiecutter-pypackage`_: A fork with separate requirements
   files rather than a requirements list in the ``setup.py`` file.

* `briggySmalls/cookiecutter-pypackage`_: A fork using Poetry_ for neat package
   management and deployment, with linting, formatting, no makefiles and more.

* `zillionare/cookiecutter-pypackage`_: A template containing Poetry_, Mkdocs_,
   Github CI and many more. It's a template and a package also
   (can be installed with `pip`)

* Also see the `network`_ and `family tree`_ for the original repo. (If you
  find anything that should be listed here, please add it and send a
  pull request!)

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _CHANGELOG: https://github.com/imAsparky/cookiecutter-py3-package/blob/main/docs/source/CHANGELOG.md
.. _cookiecutter-py3-pypackage tutorial: https://cookiecutter-py3-package.readthedocs.io/en/latest/tutorial.html
.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage
.. _Conventional-Commits:  https://www.conventionalcommits.org/en/v1.0.0/
.. _Diataxis: https://diataxis.fr/
.. _Mkdocs: https://pypi.org/project/mkdocs/
.. _Poetry: https://python-poetry.org/
.. _pre-commit: https://pre-commit.com/
.. _Projects: https://github.com/imAsparky/cookiecutter-py3-package/projects
.. _PyPi: https://pypi.python.org/pypi
.. _pyup.io: https://pyup.io/
.. _quickstart: https://cookiecutter-py3-package.readthedocs.io/en/latest/how-to/how-to-quickstart.html
.. _Read the Docs: https://readthedocs.io/
.. _Repo Status: https://www.repostatus.org/
.. _Sphinx: http://sphinx-doc.org/
.. _Test-PyPi: https://test.pypi.org/
.. _Tox: http://testrun.org/tox/


.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage
.. _`zillionare/cookiecutter-pypackage`: https://zillionare.github.io/cookiecutter-pypackage/
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
