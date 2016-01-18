"""
Notes on using salt-cloud

we want to configure two files in /etc/salt:

`cloud.providers` - details the rackspace login etc
`cloud.profiles` - details which type of machine we are going to build

ultimately we want to run::

  salt-cloud -p <profile_name> foobar -C cloud.providers -V cloud.profiles 

And see a instance of a rackjsapce profile called foobar be created (and charged !)



template variables:

profile_name : in cloud.profiles, names the image / profile to build

provider_ref: defined in cloud.providers, is the provider reference
              it is thoerietcially possible to have passwords for many logins

masterfqdn: fqdn for salt-master host

userid: username to login to rackspace

tenantid : id NUMBER

apikey: secret key from control panel 
"""

pass
