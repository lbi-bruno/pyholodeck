pyholodeck
==========

Holodeck is an attempt to write an immutable server build chain for Python packages.

We build locally a virtualenv holding the python package we care about, and convert that and its python interpreter etc into a .deb.  Alternatively we wrap that into a Docker Image.

Finally we allow for configuration and rollout via SaltStack (Ansible tryout coming) 

In short we can produce reusable build arifacts for Python from a setup.py based package.

