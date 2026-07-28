=========
Glossary
=========

This page collects short, beginner-friendly definitions of the Git terms used
throughout the :ref:`git-workflow` and :doc:`tasks` pages. It is not meant to
be exhaustive - for more detail see the
`Git documentation <https://git-scm.com/doc>`_ or the
`Atlassian Git tutorials <https://www.atlassian.com/git>`_.

Repository
==========

A repository ("repo" for short) is the collection of all files belonging to a
project together with their complete history of changes. A repository can
exist purely on your own computer (a **local repository**) or on a server
(a **remote repository**, e.g. on GitLab or GitHub), and the whole point of
Git is to keep local and remote copies of a repository in sync.

Working Tree
============

The working tree (also called the "working directory") is simply the folder
on your disk where the current, checked-out files of your repository live -
the files you actually open, edit and view in PyCharm or your file explorer.
It always reflects one specific state of your project (usually the tip of
the branch you currently have checked out), plus any uncommitted changes you
have made.

Staging Area (Index)
=====================

The staging area (sometimes called the "index") is an intermediate step
between your working tree and the repository's history. Before you can turn
a change into a commit, you first have to "add" it to the staging area (in
PyCharm this often happens automatically when you answer "Add" to the
"should Git track this new file?" prompt). This lets you carefully choose
exactly which changes should be bundled together into your next commit,
rather than always having to commit everything you changed at once.

Commit
======

A commit is a saved snapshot of your project at a particular point in time,
together with a message describing what changed and why. Commits are the
building blocks of a repository's history: each commit points back to the
commit(s) that came before it, forming a chain (or graph) that lets Git
reconstruct the entire history of the project and lets you jump back to any
earlier state if needed.

Branch
======

A branch is simply a named, movable pointer to a specific commit. The
default branch is usually called ``main``. When you want to work on a new
feature without disturbing the stable state of the project, you create a new
branch (see the *Create Branch* step of the :ref:`git-workflow`), make your
commits there, and only merge them back into ``main`` once you and your
reviewer are happy with the result. Branches are cheap to create and are the
main mechanism Git offers for isolating work in progress.

Remote
======

A remote is simply a version of your repository that is hosted somewhere
else, usually on a server such as GitLab or GitHub, so that you and your
collaborators can all synchronize with it. A repository can have several
remotes (for example if you want to keep in sync with more than one server),
but in this workshop you will normally only deal with a single one.

Origin
======

``origin`` is just the conventional default name that Git gives to the
remote repository you originally cloned from (or explicitly added first).
There is nothing magic about the name itself - it is a label, and
technically you could call it anything - but almost everyone keeps calling
it ``origin`` by convention, so that is what you will see in commands like
``git push origin main``.

Upstream
========

"Upstream" refers to the repository (usually a remote, such as ``origin``)
that your local branch is tracking, i.e. the repository you pull updates
from and push your own changes to. In the context of this workshop, "the
upstream server" and "``origin`` on GitLab" mean the same thing. You will
also encounter the term "upstream" in the phrase **pull request / merge
request**, where it describes the target repository/branch that a change
should be merged into.

HEAD
====

``HEAD`` is Git's name for "the commit you currently have checked out", i.e.
your current position in the repository's history. Most of the time
``HEAD`` simply points at the tip of whichever branch you have checked out
(so moving ``HEAD`` and moving the branch pointer happen together as you
commit), but Git also lets you check out an individual commit directly, in
which case ``HEAD`` points at that commit instead of at a branch.

Merge
=====

Merging is the process of combining the changes from one branch into
another - for example, taking the commits you made on your feature branch
and integrating them into ``main`` (see the *Merge Branch* step of the
:ref:`git-workflow`). Git automatically figures out how to combine the
changes and creates a new "merge commit" that has both branches as its
parents. If the same lines of a file were changed differently on both
branches, Git cannot decide on its own which version is correct and asks you
to resolve the resulting **merge conflict** by hand.

There is also ``rebase``, a more advanced alternative to merging that
rewrites your branch's commits on top of another branch instead of creating
a merge commit. Rebasing can produce a tidier, linear history, but it is
more error-prone for beginners and is out of scope for this workshop -
``merge`` is all you need for now.
