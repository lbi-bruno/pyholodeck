Salt and State
==============

Recap
-----

So far we have covered the basics of how salt works (It puts a service called a 
`minion` onto a host, and that minion calls back to a 0MQ server for instructions from
a salt-master)

We can build minions manually (boo-hiss) or we can use salt-cloud to build VMs in 
our provider of choice.  

Then we can write simple modules that just do-stuff on the minions.  There are a lot 
of these.  

While most of the time this is used for server config, in fact this is an ad-hoc 
remote execution setup.  And it knocks `fabric` into a cocked-hat.


One minor issue
---------------

OK, OK. Security. Its a biggie. The salt team has written it's own security setup.
It has been reviewed.  But salt is growing at such a pace, and the sheer difficulty of
doing this right indicates that salt *could* face a big, stonking hole in the future.

Its worth bearing in mind, especially as *everything runs as root* (!).

However security is a trade off, and salt brings a lot to the party and looks to be making 
simple security choices.  I am unable to compare it to chef or puppet, however my previous
choice of fabric relied on ssh - which is a real battle-tested comms system.

In the end, if you have a bunch of servers automated, I suspect that rogue injection of commands
into zeroMQ is less likely than attacking salt-master directly.

So I will stick with it.


Managing State
--------------

OK. I could issue one command after another, `expect`-style to create my remote servers.

But that would be the *old-way*.  


So now we manage state with config files, and let the minion work out how to get there.

I would recommend reading this now, or very soon http://docs.saltstack.com/ref/states/

top.sls
-------

The top file determines which state files are going to be synched with which minions.

/srv/salt/top.sls::

   base:
     '*':
        - nginx

Now, that means every machine we have will get nginx installed on it (maybe not great)
Next we need to define the nginx *state* that we want.


/srv/salt/nginx/init.sls file::

   $ ls /srv/salt/nginx/
   init.sls  nginx.conf

/srv/salt/nginx/init.sls::

    nginx:
      pkg:
        - installed
      service:
        - running
        - enable: True
        - require:
          - pkg: nginx
        - watch:
          - file: /etc/nginx/nginx.conf

    /etc/nginx/nginx.conf:
      file.managed:
        - source: salt://nginx/nginx.conf

/srv/salt/nginx/nginx.conf::

    user www-data;
    worker_processes 4;
    pid /var/run/nginx.pid;

    events {
           worker_connections
    ...


Now we install it::

    <salt-master>$ sudo salt 'myinstance' state.highstate

And after a while we can visit the host in a browser:


.. figure::  https://raw.github.com/mikadosoftware/screengrab/master/screenshots/salt-nginx.png
   :width: 25 %
