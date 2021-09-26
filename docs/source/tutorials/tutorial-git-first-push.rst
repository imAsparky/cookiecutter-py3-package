.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: cookie-create-pkg ; Index


.. _create-first-git-push:
========================
Create GitHub First Push
========================


Pre-requisites
==============

A `GitHub <https://github.com/join>`_ account.

:ref:`Create a GitHub repository.<create-GH-repo>`

:ref:`Create a cookiecutter-py3-package.<cookie-create-pkg>`


.. _create-GH-repo-tutorial:
Tutorial
========


.. _git-CLI-push-options:
GitHub Local Repository CLI Push Options
----------------------------------------

After creating your GitHub repository and cookiecutter-py3-package,
you have several options to get your package initialised and pushed into
your repository.

.. important::

  Replace `imAsparky/my-new-package.git`
  with `<your-repo-name>/<your-package-name>.git`

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you have used the default package creation setting:

.. code-block:: bash

   automatic_set_up_git_and_initial_commit [y]:


|

Getting ready for your first push to GitHub is quite simple.

.. code-block::

    cd my-new-package
    git reflog
    git push -u origin master

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Or use options provided by GitHub.

|

Quick setup — if you’ve done this kind of thing before.


.. tab:: HTTPS

    .. code-block:: bash

        git clone https://github.com/imAsparky/my-new-package.git

.. tab:: SSH

    .. code-block:: bash

        git clone git@github.com:imAsparky/my-new-package.git


.. code-block:: bash
    :caption: **…or create a new repository on the command line**

    git init
    git add -A
    git commit -m "chore(git): Initial Commit"
    git branch -M main
    git remote add origin git@github.com:imAsparky/my-new-package.git
    git push -u origin main

.. code-block:: bash
    :caption: **…or push an existing repository from the command line**

    git remote add origin git@github.com:imAsparky/my-new-package.git
    git branch -M main
    git push -u origin main

.. code-block:: bash
    :caption: **…or import code from another repository**

    This option is not supported here.


Whats next?
-----------

Check out our other :ref:`Tutorials<tutorial-index>` for more information on
how to get the most out of your cookiecutter package.
