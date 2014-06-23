'''
Created on Jun 18, 2014

@author: d

Influenced by:
    https://GetHub.com/Xeoncross/lowendscript/setup-debian.sh
'''

import os.path
import sys
import simplejson as json

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
    DEBUG = False
    LOCALE = "en_US.UTF-8"
    TIMEZONE = "EST"
    
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
                    'iptables' : '/etc/network/if-pre-up.d/iptables',
                    'zoneinfo/': '/usr/share/zoneinfo/',
                    'localtime': '/etc/localtime'
                 }
    Apt = None
    
    def __init__(self,host=None,domain=None,sshport=None,colorize=False,DEBUG=False):
        '''
        Basic script operations
        '''
        #global DEBUG
        self.DEBUG = DEBUG
        
        if host is not None:
            self.HOST = host.split('.')[0]
        if domain is not None:
            self.DOMAIN = domain.rstrip('.').lstrip('.')
            
        # TODO: make sure sshport is numberic
        if (sshport is not None):
            self.SSHPort = sshport
        
        self.COLORIZE = colorize
        self.Apt = myaptclass.myaptclass(DEBUG=DEBUG)
    
    def loadConfigFile(self,filename=None):
        #try:
            tmpstr=open(filename,'r').read()
        #except:
            self.print_warn('Error occured while reading config file!')
        #    return False
            self.loadConfigString(tmpstr)
    
    def loadConfigString(self,definition=None):
        """
        :param definition: string with JSON formated configuration
        
        """
        self.configdata = json.loads(definition)
        if self.DEBUG:
            self.print_debug('json is type %s ' % self.configdata)
                
    def dorun(self,cmd,fake_return=True):
        if self.DEBUG:
            self.print_debug('[Basic]<CMD> '+cmd)
            return fake_return
        else:
            return os.system(cmd)
        
    def fixLocale(self,mylocale=None):
        ''' Adjust the servers locale settings
        '''
        # TODO: Decide if multipath-tools is needed
        if mylocale is None:
            mylocale = self.LOCALE
            
        self.dorun('export LANGUAGE='+mylocale)
        self.dorun('export LANG='+mylocale)
        self.dorun('export LC_ALL='+mylocale)
        self.dorun('locale-gen '+mylocale)
        
        # TODO: Determin if we still need to dpkg-reconfure even if we locale-gen
        self.dorun('dpkg-reconfigure locales')
    
    def fixTimeZone(self,mytimezone=None):
        # TODO: Determine if time zone can be programmatically set
        
        # TODO: Handle Basic.TIMEZONE
        
        if mytimezone is not None:
            # ln -sf /usr/share/zoneinfo/EST /etc/localtime ## for Eastern Standard Time
            if os.path.lexists(os.path.normpath( os.path.join(self.FILEPATH['zoneinfo/'],mytimezone) )):
                self.dorun('ln -sf '+os.path.normpath( os.path.join(self.FILEPATH['zoneinfo/'],mytimezone) )+' '+self.FILEPATH['localtime'])
                return
            
        self.dorun('dpkg-reconfigure tzdata')
        
    def print_debug(self,outtext):
        if self.DEBUG:
            sys.stderr.write('DEBUG: '+outtext+'\n')
            
    def print_info(self,outtext):
        if self.showInfo:
            sys.stdout.write(outtext+'\n')
    
    def print_warn(self,outtext):
        if self.showWarn:
            sys.stderr.write(outtext+'\n')

    def print_error(self,outtext):
        if self.showError:
            sys.stderr.write(outtext+'\n')
            
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
            
        res = self.dorun('which "'+checkfile+'" 2>/dev/null')
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
            
        res = self.dorun('which "'+checkfile+'" 2>/dev/null')
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
