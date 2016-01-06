#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Create .deb files from python venvs as artifacts for deployment

app_path is where we create the virtual env
and it is also the destination for the final target venv.
We cannot avoid this - .deb creates it from dirs

'''

import os
#import fabric
import pprint

class Deployment(object):
    BASE_PATH = '/mikado'

    def __init__(self, app_name):
        self.app_name = app_name.lower()
        self.pkg_name = 'mikado-' + self.app_name
        self.app_path = os.path.join(self.BASE_PATH, self.app_name)
        self.venv_path = self.app_path
        #: where we will extract the git source to before runing setup
        self.src_path = os.path.join(self.app_path, self.pkg_name)
        #: the interpreter in this venv
        self.python_exe = os.path.join(self.venv_path, 'bin/python')
        self.cmds = []
        
    #for now just build bash commands for later
    def prepare_venv(self):
        self.cmds.append('rm -rf {}'.format(self.venv_path))
        self.cmds.append('mkdir -p {}'.format(self.venv_path))
        #chown
        self.cmds.append('virtualenv -p {} {}'.format(
                                               '/usr/bin/python',
                                               self.venv_path)
                        )
        #copy package?
        self.cmds.append('cp -r /root/projects/pyholodeck/holo/example_pkg/ {}'.format(self.app_path)) 
        self.cmds.append('cd {}'.format(self.src_path))
        self.cmds.append('{} setup.py install'.format(self.python_exe))
        self.cmds.append("fpm -s dir -t deb -n {} {}".format(
                                               self.pkg_name,
                                               self.venv_path
                        ))

d = Deployment('wizardapp')
d.prepare_venv()
pprint.pprint(d.cmds)

