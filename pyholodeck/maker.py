#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Create .deb files from python venvs as artifacts for deployment

app_path is where we create the virtual env and it is also the
destination for the final target venv.  We cannot avoid this - .deb
creates it from dirs

todo: convert to run autmaotically within python (not pront cmds)
todo: discvover postinst files and add as cmd switches to fpm
todo: have some core service that postinst can call (fabric?)
todo: chain to build servers

'''

import os
#import fabric
import pprint
import time

def gitfetch(url, parentfolder):
    '''Given a git url, retrieve to `parentfolder` 
    '''
class SubCmd(object):
    '''Smoothly act as store of a subprocess cmd

    we want to have same command as a list for non-shell 
    and in friendly form.

    nb Its a lot easier to .join a list than parse a string
    '''
    def __init__(self, cmdlist, pythonstmt=None, args=None):
        self.cmdlist = cmdlist
        self.pythonstmt = pythonstmt
        self.args = args
            
    def __repr__(self):
        return " ".join(self.cmdlist)
    
        

class Deployment(object):

    '''A big wrapper around different stages in making the 
       python package into a .deb

    We are building a simple solution
    1. We build on local disk, in the expected locations, a venv
       representing the state of the venv we want eventually to deploy
    2. We wrap that venv, with the python interpreter etc, into 
       a `.deb` file (tarball basically).  
    3. We define a `saltstack` file that will deploy the .deb file 
       artifact to our infrastructure.  This file will define how to
       create the .ini / .conf files that will be put into well-known
       locations for the configuration of the package.

    4. We define in the package the conf template for reference 
       

    Alternatively the artifact can be a Docker image that contains 
    our .deb file


    '''
    #: the root where the final .deb installed code will get put
    #: it is also, for ease of building .debs, where we put the code
    #: so the .deb making stage can find it
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
        #: build list of cmds to run.
        for cmd in (
                SubCmd(['rm', '-rf', self.venv_path]),
        
                SubCmd(['mkdir', '-p', self.venv_path]),
        
                SubCmd(['mkdir', '-p', self.src_path]),
                
                SubCmd(['virtualenv', '-p', '/usr/bin/python',
                                               self.venv_path]),
                
                #replace with with
                #self.cmds.append('. {}/bin/activate'.format(self.venv_path))
        
                SubCmd(['git', 'clone', self.giturl, self.src_path]),
                
#                SubCmd(['cd', self.src_path]),
                SubCmd([], os.chdir, [self.src_path]),
                #: dependancies
                SubCmd([self.pip_exe, 'install', '-r', 'requirements.txt']),
                
                SubCmd([self.python_exe, 'setup.py', 'install']),
                SubCmd(['fpm', '-s', 'dir', '-t', 'deb', '-n',
                                               self.pkg_name,
                                               self.venv_path])
        ):
            self.cmds.append(cmd)

def demo():
    d = Deployment('pyhello',
                   'github:mikadosoftware/pyhelloworld.git')
    d.prepare_venv()
    import subprocess
    for cmd in d.cmds:
        print cmd, "..."
        time.sleep(1.5)
        if not cmd.args:
            print subprocess.check_call(cmd.cmdlist)
        else:
            cmd.pythonstmt.__call__(*cmd.args)

if __name__ == '__main__':
    demo()                

