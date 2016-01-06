
Goals
To define a process and automated tool (deb-build-app) to 

* work on a target host OS
* prepare the build dependancies
* extract from git the desirted source code and static files
* prepare all as a venv
* package the vevn as a deb
* prepare suitable postinstall files to connect to supervisord 
* prepare postinstall files to get correct configuration 

We shall demonstrate this with a simple flask app


using Ansible as a slave not a master
-------------------------------------
This ought to be some kind of Brian's Law by now.  A framework written in any language will eventually try to implement a crippled copy of itself in the framework, using YAML.::

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
b e much much easier to read.

Sort of Ansible Tower-Defence


We need to run the venv python binary, from within the folder holding setup.py to do an install
Then we can verify the venv holds the package by looking at venv's site-packages


Now we create the fpm deb



eatmydata - this is an *advanced* utility that will turn off fync() calls - thus any process that makes build files in memory, 
or syncs files to disk when really we only care about the final output, not recvoiering, can spped up - estiamtes by 1/3.
http://people.skolelinux.org/pere/blog/Speeding_up_the_Debian_installer_using_eatmydata_and_dpkg_divert.html

We can tell we are in a venv buy looking at sys module - sys.prefix gives us the prefix form the bin/python back and real_prefix gives us the prefix it was when the binary was coipied over.
