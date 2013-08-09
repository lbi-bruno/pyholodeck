Install salt-master
===================


I am focusing on rackspace for salt-cloud.

Initially I build a cloud server, and then convert it into a salt-master.
You could use your laptop, but thats not a particularly long term solution.

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


Bring up our first minion
-------------------------


::

  sudo salt-cloud -p openstack_512 myinstance

We are telling salt-cloud to create a minion, using the openstack_512 profile 
defined above, and the provider details, and call that minion myinstance.

When it exists we can do lots of fun things with the minion, from salt-master.

::

  171  salt '*' test.ping
  172  sudo salt '*' test.ping
  173  sudo salt 'myinstance' test.ping
  174  sudo salt 'myinstance' sys.doc
  175  sudo salt 'myinstance' timezone.get_zone
  176  sudo salt 'myinstance' cmd.run 'ls -l /tmp'
  177  sudo salt 'myinstance' pkg.install emacs

This is all very well, but still fairly manual and prescriptive.  Lets move on.
