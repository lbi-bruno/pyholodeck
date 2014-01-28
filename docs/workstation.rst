Salt basics again
-----------------

I am building a salt-controlled workstation, which has my security antennae
jingling but it still seems a good idea.

I use the FreeBSD usb-stick to wipe a machine, then pull down
"bootstrap.saltstack.org" (which is a pointer to the github repo latest).

This will install saltstack (Python, SWIG, few other bits, and the saltstack repos) on our workstation.  Then we are almost ready to go.

::

   update minion to have our salt master as its master
   /usr/local/etc/salt/minion::
      
   master: salt.mikadosoftware.com

   providers:
     pkg: pkgng

Here we are altering the minion config file in two ways.  Firstly we set the
master to be salt.mikadosoftware.com.  The default behaviour is to assume
salt.<search term in /etc/resolv.conf> is the master, but I prefer to be
explicit.

Secondly, 


Note this approach is *only* needed for a laptop.  A cloud server salt-master is able to setup its own minions without regard for our attention span.




$ sudo salt-key -d cube
The following keys are going to be deleted:
Accepted Keys:
cube
Proceed? [N/y] y
Key for minion cube deleted.

matching:
>>> import socket 
>>> socket.getfqdn()
'cube.mikadosoftware.com'



Upgrading salt
--------------

upgrade master, then minions.

::

  salt --version

Use the packaging approach for the master (apt-get / pkg)




def _check_pkgng():
    '''                                                                                   
    Looks to see if pkgng is being used by checking if database exists                    
    '''
    return os.path.isdir('/usr/local/etc/pkg/repos/')
