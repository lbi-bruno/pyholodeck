Writing your first salt module
==============================

Salt modules are simply python files that are executed by the running minion on
the minion-server, after being told to by the salt-master.  Some environment and
configuration can be passed in, but most of what we need is available by
introspecting the minion-host.


Where to put a salt module?
---------------------------

First create `{FILES_ROOT}/_modules/`.
`FILES_ROOT` is defined in /etc/salt/master, and defaults to `/srv/salt`

Now create a python module in the _modules directory, such as `pbrian.py`

Simplest possible salt module::

  import salt

  def hello()
      return "hello world"


And that's it.  


Synchronise from the salt-master to the minion(s)
-------------------------------------------------

::

   salt '*' saltutils.sync_all
        ^ 
        selects which minions

    $ sudo salt 'myinstance' saltutil.sync_all
    myinstance:
        ----------
        grains:
        modules:
            - modules.pbrian
        outputters:
        renderers:
        returners:
        states:


This will synch the _modules directory (and lots else) from master to minion.
So modules are either those you have written and deployed into _modules
yourself, or are properly incorporated into the main salt repos


Now run your module on the minion
---------------------------------

::

    $ sudo salt 'myinstance' pbrian.hello
    myinstance:
        hello world

Hooray!

So lets recap.

We can manually build a salt-master.
We can then auto build any number of minions (up to our credit card limit !)
Then we can write a python module to do *anything* on the minion, deploy it and 
get its output returned to us.


Next steps
----------

* Better Python Integration.
* Actually building our build server.

