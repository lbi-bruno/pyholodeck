#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Create .deb files from python venvs as artifacts for deployment

app_path is where we create the virtual env
and it is also the destination for the final target venv.
We cannot avoid this - .deb creates it from dirs

todo: convert to run autmaotically within python (not pront cmds)
todo: discvover postinst files and add as cmd switches to fpm
todo: have some core service that postinst can call (fabric?)
todo: chain to build servers

'''

import os
#import fabric
import pprint

def gitfetch(url, parentfolder):
    '''Given a git url, retrieve to `parentfolder` 
    '''
    

class Deployment(object):
    BASE_PATH = '/mikado'

    def __init__(self, app_name, giturl):
        self.app_name = app_name.lower()
        self.pkg_name = 'mikado-' + self.app_name
        self.app_path = os.path.join(self.BASE_PATH, self.app_name)
        self.venv_path = self.app_path
        #: where we will extract the git source to before runing setup
        self.src_path = os.path.join(self.app_path, self.pkg_name) + "-src"
        #: the interpreter in this venv
        self.python_exe = os.path.join(self.venv_path, 'bin/python')
        self.pip_exe = os.path.join(self.venv_path, 'bin/pip')
        self.giturl = giturl
        self.cmds = []
        
    #for now just build bash commands for later
    def prepare_venv(self):
        self.cmds.append('rm -rf {}'.format(self.venv_path))
        self.cmds.append('mkdir -p {}'.format(self.venv_path))
        self.cmds.append('mkdir -p {}'.format(self.src_path))        
        #chown
        self.cmds.append('virtualenv -p {} {}'.format(
                                               '/usr/bin/python',
                                               self.venv_path)
                        )
        #replace with with
        self.cmds.append('. {}/bin/activate'.format(self.venv_path))
        
        self.cmds.append('git clone {} {}'.format(self.giturl,
                                                  self.src_path)) 
        self.cmds.append('cd {}'.format(self.src_path))
        #: dependancies
        self.cmds.append('{} install -r requirements.txt'.format(self.pip_exe))
        self.cmds.append('{} setup.py install'.format(self.python_exe))
        self.cmds.append("fpm -s dir -t deb -n {} {}".format(
                                               self.pkg_name,
                                               self.venv_path
                        ))

d = Deployment('pyhello',
               'github:mikadosoftware/pyhelloworld.git')
d.prepare_venv()
pprint.pprint(d.cmds)

