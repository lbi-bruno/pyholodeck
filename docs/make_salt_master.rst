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

Basic Directory Layout 
----------------------

There are two directorys to worry about

* /etc/salt - basic config for both cloud, master, minion
* /srv/salt - location of all the files we are going to put on minion. (Its more complex than that but thats the simplest explantion)

configure the cloud
-------------------

In `/etc/salt` we want to create / adjust two files, `/etc/salt/cloud.providers`
holds credentials and identifiers for our cloud account.  `/etc/salt/cloud.profiles` 



salt-cloud is going through a revamp of it's configuration, and the new stuff is not quite ready for prime time.  This works to date.


`/etc/salt/cloud.providers` ::

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


`/etc/salt/cloud.profiles`::

    mikado_512:
        provider: mikado-rackspace
        size: 512MB Standard Instance
        image: Ubuntu 12.04 LTS (Precise Pangolin)

I have linked this minimal profile called mikado_512, to the rackspace account
mikado-rackspace, with the sizes and images configured from (tbd).


Bring up our first minion
-------------------------


::

  sudo salt-cloud -p mikado_512 minone

We are telling salt-cloud to create a minion, using the mikado_512 profile 
defined above, and the provider details, and call that minion minone.

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
