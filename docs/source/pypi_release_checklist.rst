======================
PyPI Release Checklist
======================

*Copyright 2015, Audrey Roy Greenfeld*


Before Your First Release
-------------------------

#. Register the package on PyPI:

    .. code-block:: bash

        python setup.py register

#. Visit PyPI to make sure it registered.

For Every Release
-------------------

.. todo::
    An automatic CHANGELOG now handles history—another small tutorial
    describing how-to create a release is required.

    See `Issue 36 <https://github.com/imAsparky/cookiecutter-py3-package/issues/36>`__.

#. Update HISTORY.rst


#. Commit the changes:

    .. code-block:: bash

        git add HISTORY.rst
        git commit -m "Changelog for upcoming release 0.1.1."

#. Install the package again for local development, but with the new version number:

    .. code-block:: bash

        python setup.py develop

#. Run the tests:

    .. code-block:: bash

        tox

#. Push the commit:

    .. code-block:: bash

        git push

#. Push the tags, creating the new release on both GitHub and PyPI:

    .. code-block:: bash

        git push --tags

#. Check the PyPI listing page to make sure that the README, release notes, and
   roadmap display properly. If not, try one of these:

    #. Copy and paste the RestructuredText into http://rst.ninjs.org/ to find
       out what broke the formatting.

    #. Check your long_description locally:

        .. code-block:: bash

            pip install readme_renderer
            python setup.py check -r -s

#. Edit the release on GitHub (e.g. https://github.com/imAsparky/cookiecutter/releases).
   Paste the release notes into the release's release page, and come up with a title for the release.
