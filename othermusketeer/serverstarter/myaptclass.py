'''
Created on Jun 18, 2014

@author: d
'''

import os

class myaptclass(object):
    didUpdate = False
    def __init__(self):
        pass
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
        
                    
