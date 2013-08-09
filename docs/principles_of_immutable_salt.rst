Immutable salt
==============

I intend to use salt as an automated build tool, for which I wish to use
the concept of `immutable servers <http://www.thoughtworks.com/insights/blog/rethinking-building-cloud-part-4-immutable-servers>`_.

Mostly its pretty simple - have one automated build system to build a (virtual) server from scratch,
and make sure that server is *exactly the same* each time.  Same OS, same package installs, same config files.

Change something?  Thats a new version - a *different* immutable server.

Need to upgrade nginx, then your SaaS app needs to get pulled off v.1.2.3 servers and onto v.1.2.4

You do *not* upgrade nginx in-situ.


Thats it really.

So how to do it?
================


