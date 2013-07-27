HoloDeck
========

Holodeck is based on the `rant <http://hynek.me/articles/python-app-deployment-with-native-packages/>`_ of Python Core Committer Hynek Schlawack.

It also owes a lot to `parcel <parcel.readthedocs.org>`_ - not necessarily that
any of the codebase is the same but for the sheer get on and do it.  Sadly, I
could not muster the energy to cross the hg/git divide so instead of
contributing patches I simply redid.

HoloDeck is an attempt at a pun - the core idea is to wrap up an entire virtualenv and pass it from host to host.  In other words we `enclose virtual environments.`  I never said it was a good pun.

The problem
-----------

We want to build nice Python (web) packages in the `micro-services` style.
This usually means lots of autonomous, independant web services, often with 
failovers, and load balancers.

So the deployment of these is more complex than just running on a local port.

But we want it to be simple and automated.


So, we need to build many hosts, provision them correctly, then build our
most recent commit, make sure it is the same on each host, configure it differently, then run functional tests over it.

Salt will certainly help there.




Three main stages of development
================================

* We will use salt-cloud to create all the environments during the build process

* We will build a Hynek-like holodeck to create bundled virtualenvs.

* We will distribute the testing of the services, especially at the HTTP level.
  They will use `webtest` as a starting point.




Contents

.. toctree::
   :maxdepth: 2

   salt-cloud
   holodeck
   tester

