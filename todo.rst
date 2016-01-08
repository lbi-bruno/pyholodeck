
Goals
=====

To define a process and automated tool (deb-build-app) to 

* work on a target host OS
* prepare the build dependancies
* extract from git the desirted source code and static files
* prepare all as a venv
* package the vevn as a deb
* prepare suitable postinstall files to connect to supervisord 
* prepare postinstall files to get correct configuration 

We shall demonstrate this with a simple flask app

target host OS
--------------
Leave as is for now. Need to run openstack instacnes or VMs to do that nicely.

Prepare the build dependancies
------------------------------
Essentially this is apt-get <list of deps>
The difficult part is getting the list, and thats a developer responsibility.

Extract the (git) source code
-----------------------------
This will mean wrapping git - Popen will do for now, but we should look at moving to calling ansible plays?
We can then do any further adjustments to the source code (compile LESS?)

Prepare a Venv
--------------

The basic plan is to build a directory holding a venv, which
Holds a complete python interpreter and libraries, as well
As holding (in site-packages) the various their party pip libraries 
We pulled in and out specific code.  All this is under one directory.

We then just wrap that dir in a .deb file, and can use it to deploy to 
wherever we want, with standard tools.


Build the .deb file
-------------------

This is relatively simple.  fpm does the hard work 

Run pre/post install scripts
----------------------------

One script will apply the config to the /etc did in the app

Maybe another will add us to supercisrd 

using Ansible as a slave not a master
-------------------------------------
This ought to be some kind of Brian's Law by now.  

'''A framework written in any language will eventually try to implement a crippled copy of its own language, inside the framework, using YAML'''

I first remeber seeing this in magic-Django, with those awful SQL-DSLs. SAlt does this too. Puppet is nothing but DSL.
Its wrong. Use an API.

::

   - name: here, 'users' contains the above list of employees
     mysql_user: name={{ item[0] }} priv={{ item[1] }}.*:ALL append_privs=yes password=foo
     with_nested:
       - "{{users}}"
       - [ 'clientdb', 'employeedb', 'providerdb' ]

The above is from http://docs.ansible.com/ansible/playbooks_loops.html#standard-loops and is some kind of in-playbook
loop that, I don't know. Something to do with users.

I am not 100% sure I am right but I swear that learning yet another half-baked DSL when I could just, y'know, use Python 
or at least access the shell undernesath as the mysql-user module probably does anyway.

So I prefer a different approach - where I will run Python, that will run playbooks as needed, and will probably 
be much much easier to read.

Sort of Ansible Tower-Defence

Ansible API usage
-----------------



We need to run the venv python binary, from within the folder holding setup.py to do an install
Then we can verify the venv holds the package by looking at venv's site-packages


Now we create the fpm deb



eatmydata - this is an *advanced* utility that will turn off fync() calls - thus any process that makes build files in memory, 
or syncs files to disk when really we only care about the final output, not recvoiering, can spped up - estiamtes by 1/3.
http://people.skolelinux.org/pere/blog/Speeding_up_the_Debian_installer_using_eatmydata_and_dpkg_divert.html

We can tell we are in a venv buy looking at sys module - sys.prefix gives us the prefix form the bin/python back and real_prefix gives us the prefix it was when the binary was coipied over.

Running daemons 
---------------

We want two approaches, to support services that have not been daemonised, and to support services that have been daemonised.
Daemons are specific things, with handlers for SIGINT flags etc, and while we *can* wrap python scripts in handlers like we do 
for similar CLIs, its sometimes *better* to just let the scripts run in the terminal, dumping to stdout and have something like supervisord handle the rougher edges.

THis is the Haynek/12 factor app idea, and is perfectly *fine*, although it is well worth thinking how to support SIG style flags in your script.

I will build supervisord under systemd (whose job it is to manage daemons) , 
and then have supervisord run the majority of our python services, however 
slowly migrating the more important services to their own daemonisation.



