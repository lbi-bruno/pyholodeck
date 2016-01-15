HoloDeck
========

Holodeck is an attempt to write an immutable server build chain
for Python packages.

At the moment I have a means to build .deb packages from a
python package (say hosted on github, with a working `setup.py` file)

The build can occur on a spun up cloud server thus meaning the build
willcorrectly target the final destination OS, no matter what your
laptop runs.

Then we can spin up a destination cloud server and using saltstack / ansible (in transition) we can deploy the package, and configure it using holo-config)

I have introduced a Docker build after this, so the final artifact can be either .deb or a docker image.   

This .deb file can then be taken to another server, built in the cloud
using salt also, and installed. That way we can build our version of a
package once, and move it from test to production, confident we are
using the same code, same binary on live as we tested.


Holodeck is based on the `rant
<http://hynek.me/articles/python-app-deployment-with-native-packages/>`_
of Python Core Committer Hynek Schlawack.

It also owes a lot to `parcel <parcel.readthedocs.org>`_ - not
necessarily that any of the codebase is the same but for the sheer get
on and do it.  Sadly, I could not muster the energy to cross the
hg/git divide so instead of contributing patches I simply redid.  They
have better looking docs too.

HoloDeck is an attempt at a pun - the core idea is to wrap up an
entire virtualenv and pass it from host to host.  In other words we
`enclose virtual environments.` I never said it was a good pun.

The idea is to build a new wrapped venv for every commit, and install
it onto immutable servers as it progresses through testing.

I hope this will facilitate more Python (web) packages in the
`micro-services` style.



Contents

.. toctree::
   :maxdepth: 1


   make_salt_master
   first_module
   improving_modules
   principles_of_immutable_salt
   salt_and_state

