Improved Salt Modules
=====================

We now want to get a little more useful.

Developing locally
------------------

Synching and running commands remotely is all very well, but sometimes we need to develop locally
to the salt-master.  That's fine::


   We can fiddle with the local minion modules dir found here:

      /var/cache/salt/minion/extmods/modules/pbrian.py

   Or we can alter local `\etc\salt\minion` file and add our chosen location to `modules_dir`

This is the simplest and fastest means to develop a module, at least until
we delve deeper into saltstack.   Do remember that a sync will overwrite your changes !!


Making a minion do something useful
-----------------------------------

Firstly we shall look at `grains` ::

 
    Grains
      Static bits of information that a minion collects about the system when the minion first starts. 


I can use them from the CLI::

    sudo salt '*' grains.ls

However this is more fun::


   import salt

   def show_grains():
       return __grains__

Which gives us::

    /snip
    cpu_model:
        AMD Opteron(tm) Processor 4170 HE
    cpuarch:
        x86_64
    defaultencoding:
        UTF-8
    defaultlanguage:
        en_US
    /snip

or even::

   import salt

   def show_grains():
       return __grains__['pythonversion']


So, let's sync up the current local pbrian.py with our minion.

::

   sudo salt 'myinstance' saltutil.sync_all

Running salt programmatically
-----------------------------

Let's write a simple python script, in our home-dir.

::

  import salt.client
  client = salt.client.LocalClient()
  ret = client.cmd('myinstance', 'show_grains',[])
  print ret

gives us::

   {'myinstance': [2, 7, 3, 'final', 0]}

A python dict, returned from a remote minion, ready for manipulation here.


