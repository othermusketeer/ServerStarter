'''
Created on Jun 18, 2014

@author: d
'''

import os
import sys

class myaptclass(object):
    didUpdate = False
    DEBUG = False
    
    def __init__(self,DEBUG=False):
        self.DEBUG = DEBUG
        pass
    
    def dorun(self,cmd,fake_return=True):
        if self.DEBUG:
            self.print_debug('[myaptclass]<CMD> '+cmd)
            return fake_return
        else:
            return os.system(cmd)
        
    def print_debug(self,outtext):
        if self.DEBUG:
            sys.stderr.write('DEBUG: '+outtext+'\n')
            
    def print_info(self,outtext):
        if self.showInfo:
            sys.stdout.write(outtext)
    
    def print_warn(self,outtext):
        if self.showWarn:
            sys.stderr.write(outtext)

    def print_error(self,outtext):
        if self.showError:
            sys.stderr.write(outtext)
                    
    def clean(self):
        os.system('apt-get -q -y autoclean')
        os.system('apt-get -q -y clean')
        
    def update(self):
        os.system('apt-get -q -y update')
        self.didUpdate = True
        
    def upgrade(self):
        self.update()
        os.system('apt-get -q -y upgrade')
        os.system('apt-get -q -y autoremove')
        
    def setUpProxy(self,phost=None,pport=3142):
        # TODO: setup apt-cahcer-ng
        pass
    
    def install(self,packages):
        packageString = ' '.join(packages)
        os.system('apt-get -q -y install '+packageString)
        
    def remove(self,packages,purge=False):
        purgestring=" --purge "
        if not purge:
            purgestring = ""    
        packageString = ' '.join(packages)
        os.system('apt-get -q -y remove '+purgestring+packageString)    
        
                    
