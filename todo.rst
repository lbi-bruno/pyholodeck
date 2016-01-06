* read up on packaging and distribution options
* choose a mvp
* 


eatmydata - this is an *advanced* utility that will turn off fync() calls - thus any process that makes build files in memory, 
or syncs files to disk when really we only care about the final output, not recvoiering, can spped up - estiamtes by 1/3.
http://people.skolelinux.org/pere/blog/Speeding_up_the_Debian_installer_using_eatmydata_and_dpkg_divert.html

We can tell we are in a venv buy looking at sys module - sys.prefix gives us the prefix form the bin/python back and real_prefix gives us the prefix it was when the binary was coipied over.
