Salt and State
--------------

Recap
-----

So far we have covered the basics of how salt works (It puts a service called a 
`minion` onto a host, and that minion calls back to a 0MQ server for instructions from
a salt-master)

We can build minions manually (boo-hiss) or we can use salt-cloud to build VMs in 
our provider of choice.  

Then we can write simple modules that just do-stuff on the minions.  There are a lot 
of these.  

While most of the time this is used for server config, in fact this is an ad-hoc 
remote execution setup.  And it knocks `fabric` into a cocked-hat.


One minor issue
---------------

OK, OK. Security. Its a biggie. The salt team has written it's own security setup.
It has been reviewed.  But salt is growing at such a pace, and the sheer difficulty of
doing this right indicates that salt *could* face a big, stonking hole in the future.

Its worth bearing in mind, especially as *everything runs as root* (!).

However security is a trade off, and salt brings a lot to the party and looks to be making 
simple security choices.  I am unable to compare it to chef or puppet, however my previous
choice of fabric relied on ssh - which is a real battle-tested comms system.

In the end, if you have a bunch of servers automated, I suspect that rogue injection of commands
into zeroMQ is less likely than attacking salt-master directly.

So I will stick with it.


Managing State
--------------

OK. I could issue one command after another, `expect`-style to create my remote servers.

But that would be the *old-way*.  


So now we manage state with config files, and let the minion work out how to get there.


