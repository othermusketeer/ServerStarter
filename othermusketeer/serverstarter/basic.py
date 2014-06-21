'''
Created on Jun 18, 2014

@author: d

Influenced by:
    https://GetHub.comXeoncross/lowendscript/setup-debian.sh
'''

import os.path
import sys

from othermusketeer.serverstarter import myaptclass

class Basic(object):
    '''
    classdocs
    '''
    DOMAIN = "example.com"
    HOST = "host"
    IP = "x.x.x.x"
    SSHPort = 22
    UPSTREAMDNS = "x.x.x.x"
    COLORIZE = False
    
    showWarn = True
    showInfo = True
    showError = True
    
    FILEPATH = {    'hosts' : '/etc/hosts',
                    'resolv.conf' : '/etc/resolv.conf',
                    'hostname' : '/etc/hostname',
                    'init_gen_host_keys' : '/etc/init.d/ssh_gen_host_keys',
                    'version' : '/etc/debian_version',
                    'xinet.d/' : '/etc/xinet.d/',
                    'up.rules' : '/etc/iptables.up.rules',
                    'iptables' : '/etc/network/if-pre-up.d/iptables'
                 }
    
    Apt = None
    
    def __init__(self,host=None,domain=None,sshport=None,colorize=False):
        '''
        Basic script operations
        '''
        if host is not None:
            self.HOST = host.split('.')[0]
        if domain is not None:
            self.DOMAIN = domain.rstrip('.').lstrip('.')
        if (sshport is not None) and (sshport.isdigit()):
            self.SSHPort = sshport
        
        self.COLORIZE = colorize
        self.Apt = myaptclass()
        
    def fixLocale(self):
        '''
        check_install multipath-tools multipath-tools
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8
    
        # Generate locale
        locale-gen en_US.UTF-8
        dpkg-reconfigure locales
        '''
        
        os.system('dpkg-reconfigure locales')
    
    def fixTimeZone(self):
        os.system('dpkg-reconfigure tzdata')

    def dbg(self,outtext):
        global DEBUG
        if DEBUG:
            return True
        else:
            return False
        
    def print_debug(self,outtext):
        global DEBUG
        if DEBUG:
            sys.stderr.write(outtext)
            
    def print_info(self,outtext):
        if self.showInfo:
            sys.stdout.write(outtext)
    
    def print_warn(self,outtext):
        if self.showWarn:
            sys.stderr.write(outtext)

    def print_error(self,outtext):
        if self.showError:
            sys.stderr.write(outtext)
            
    def check_sanity(self):
        # check root
        try:
            euid = os.geteuid()  # @UndefinedVariable
        except OSError:
            euid = 999999999999999999999
        
        if euid != 0:
            self.print_error("Must have root permissions!")
            return False
        # check debian_version
        if not os.path.isfile(self.FILEPATH['version']):
            self.print_error("Must be a Debian distribution!")
            return False
        # Return true if everything checks out OK
        return True
    
    def check_remove(self,checkfile,touninstall,displayname=None,purge=True):
        if displayname is None:
            displayname = checkfile
            
        res = os.system('which "'+checkfile+'" 2>/dev/null')
        douninstall = False
        if res == 0:
            douninstall = True
        else:
            if os.path.isfile(checkfile):
                douninstall = True
            else:
                self.print_warn(displayname+" doesn't exist; No remove needed.")
        if douninstall:
            self.print_debug("self.Apt.install(["+' '.join(touninstall)+"])")
            self.print_info(displayname+" installed.")
    
            
    def check_install(self,checkfile,toinstall,displayname=None):
        if displayname is None:
            displayname = checkfile
            
        res = os.system('which "'+checkfile+'" 2>/dev/null')
        doinstall = False
        if res == 0:
            self.print_warn(displayname+" is already installed.")
        else:
            if os.path.isfile(checkfile):
                self.print_warn(displayname+" already exists.")
            else:
                doinstall = True
        
        if doinstall:
            self.print_debug("self.Apt.install(["+' '.join(toinstall)+"])") 
            self.print_info(displayname+" installed.")
