Adding a user to a minion
=========================

Oddly enough this is not something we need to do much - but I want to see 
for myself any changes going on.

Its more awkward than you might think.


Useful stuff
------------

::

  /etc/nginx/nginx.conf:
    file.managed:
      - source: salt://nginx/nginx.conf


This is a common state defintion found in a .sls file.  It can be translated roughly as "the name of this directive is `/etc/nginx/nginx.conf`, as the minion,
run the python function `managed()` found in `file.py`.  The github location is https://github.com/saltstack/salt/blob/develop/salt/states/file.py

The `dirroot` for salt:// is file_roots defaulted to `/srv/salt`.  So thats saying copy the file(s) at /srv/salt/nginx/nginx.conf over to the minion, and have the minion apply it to the name of the state or `/etc/nginx/nginx.conf`


.sls files are simply YAML representations of a python dict.  The YAML is converted into a python  dict and then passed into saltstack for futher processing.  THis means we could just pass in a python dict.


To manually add a user on a minion, just for a look-see::

    on salt-master:
   
    $ mkpasswd -m sha-512 mypassword
    $6$xxxxx

    then 
    
    sudo salt 'minion' shadow.set_password paultest  '$6$xxx'

    (NB use single quotes to avoid bash trying to interpret $6 etc)




We can now create a file in `master:/srv/salt` called `user.sls` (nb .sls file naming - we can name it anything we want aslong as we refernce it in top.sls.  However user.present in the yaml below is a call to function present() in module user in salt/states python package.


::

 tom:
    user.present:
        - fullname: "Tom Jones"
        - groups: 
          - sudo
        - password: "$6$KnCTpLcE/QBK$nEVZZ/6K40LawBDQ4xNtTktpcp4XoUtWoGDD0JDF5nw5pH1BZgXAuqwplCVx0dS23t3EKSHrxKRhZc55QH7tJ0"  


So We can create a state, now lets look at debugging.








Biblio
------

http://dev.mlsdigital.net/posts/SaltStackBeyondJinjaStates/
