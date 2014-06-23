from othermusketeer.serverstarter import basic

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    global DEBUG
    exampleSetup = basic.Basic(sshport=1345,colorize=False,DEBUG=DEBUG)

    exampleSetup.loadConfigFile('../bin/ServerStarter.json')    
    exampleSetup.fixLocale('en_US.UTF-8')
    exampleSetup.fixTimeZone()

DEBUG = True

if __name__ == "__main__":
    test_basic()
    