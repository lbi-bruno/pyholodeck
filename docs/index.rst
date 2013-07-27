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




Install
=======

Some notes, to be tidied up. - mostly from https://salt-cloud.readthedocs.org/en/latest/topics/rackspace.html

Installing salt onto ubunutu 12.04::

  sudo apt-get -y install python-software-properties
  sudo add-apt-repository -y ppa:saltstack/salt
  sudo apt-get update

  sudo apt-get -y install salt-master
  sudo apt-get -y install salt-minion
  sudo apt-get -y install salt-cloud
  ## delete as applicable

We now have a salt-master on a host, lets put salt-cloud up

`/etc/salt/cloud.providers.d/rackspace.conf` needs to have the following added

::

    my-rackspace-config:
      # Set the location of the salt-master
      #
      minion:
        master: saltmaster.example.com

      # Configure Rackspace using the OpenStack plugin
      #
      identity_url: 'https://identity.api.rackspacecloud.com/v2.0/tokens'
      compute_name: cloudServersOpenStack
      protocol: ipv4

      # Set the compute region:
      #
      compute_region: DFW

      # Configure Rackspace authentication credentials
      #
      user: myname
      tenant: 123456
      apikey: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

      provider: openstack

  


Contents

.. toctree::
   :maxdepth: 2

   salt-cloud
   holodeck
   tester

