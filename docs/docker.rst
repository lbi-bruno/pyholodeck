Docker and Salt and Python
--------------------------

Docker is a useful abstraction level for managing deploymebnts (just
as the holodeck is) and I want to combine the two.

Additionally I want to use SaltStack to install the applicaions etc
into docker because the scripting of a dockerfile is ... a bit
limited.

Todo
----

1. reduce config to simplest possible
2. run an e2e build from git src to docker, and that has a web server running in it.



The overview
------------

I will create a base image of a Docker image with a salt-minion in it from 
a Dockerfile

I will then update and adjust that image to hold whatever code i need using
salt instructions

I will then 'commit' those changes to a new image, labelled appropriately.

Rinse and repeat.

Building a Python Development Environment
-----------------------------------------

I will do this "properly" - which means less mucking about with my host
system and more developing on VMs.  So I will first define a salt state
that will be my Python development enviornment, y'know, 3.4, with pip
and a few other bits.

In thoery that could be the base image for releasing apps I develop on that 
dev env.

Stage 0
-------

Prepare the host to run docker and salt-master

::

   apt-get install docker


docker networking
~~~~~~~~~~~~~~~~~

https://docs.docker.com/engine/reference/run/
For performance reasons we should run in host network mode on prod.



Stage 1
-------

Prepare a base image.

::

  $ docker pull debian:jessie

This will get the latest jessie debian image locally for us.

Stage 2
-------

/foo/bar/DockerFile::


    # dockerfile to build simple salt minion
    # from which I can populate using salt and then build new docker images

    FROM debian:jessie
    RUN apt-get update
    RUN apt-get install -y salt-minion

::

    $ docker build -t mikadosoftware.com/pybase:0.0.1 .

    $ docker images

Stage 3
-------

Run the image, ensuring we start the minion and it tries to call home to master.

$ docker run --add-host=salt:192.168.0.107 \
             --hostname minion \
             --name minionname \ 
              salt-minion

pbrian@HPCube:~/projects/pyholodeck/docs$ sudo salt 'minion' test.ping
minion:
    True

add-host: will add entry to hosts file on container, so we cand route out 
hostname and name is for ease of not reading hashes.


Stage 4 
-------

Define a salt state for python


https://github.com/saltstack/salt/blob/develop/salt/modules/dockerng.py

https://www.logilab.org/blogentry/290489


http://stackoverflow.com/questions/25129553/how-can-i-validate-a-salt-minions-key-fingerprint-before-accepting-it-on-the-ma
https://docs.docker.com/engine/userguide/containers/dockerimages/


1. we 



Useful notes
------------

docker images

list containers:
  docker ps -a
delete containers
  docker rm <idNumber>

list images
  docker images
remove images
  docker rmi <imageID or tag>

You need to remove containers that xist (started or stopped) that 
are runing off images

docker run -it <image>
   interactive and ptty

http://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile
The ENTRYPOINT specifies a command that will always be executed when the container starts.

The CMD specifies arguments that will be fed to the ENTRYPOINT.

So if I use the follwoiong format for my entrypoint and cmd::

  ADD startup.sh /root
  RUN chmod 0777 /root/startup.sh
  ENTRYPOINT ["/bin/bash", "/root/startup.sh"]
  CMD ["Arg From Dockerfile"]

and have this in /root/startup.sh::

    echo "Running startup script. Args are " $1

I can run these ::

  $ docker run -it mikadosoftware.com/holobase:0.0.1
  Running startup script. Args are  Arg From Dockerfile

  $ docker run -it mikadosoftware.com/holobase:0.0.1 foo
  Running startup script. Args are  foo



GoogleBreadcrumbs
-----------------

::

    [ERROR   ] The Salt Master has cached the public key for this node, this salt minion will wait for 10 seconds before attempting to re-authenticate

    [ERROR   ] The Salt Master has cached the public key for this node, this salt minion will wait for 10 seconds before attempting to re-authenticate

This means "your salt master has not yet accepted my key"

Attach
------
docker attach nonenetcontainer
Note: You can detach from the container and leave it running with CTRL-p CTRL-q.
