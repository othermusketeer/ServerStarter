import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

    
project_version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
except:
    README = ""
if README=="":
    try:
        README = open(os.path.join(here, 'README.md')).read()
    except:
        README = ""
        
try:
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except:
    CHANGES = ""

requires = []
#requires=['pyramid>=1.3', 'pyramid_jinja2', 'wtforms', 'webhelpers']

config = {
    'description': 'Python package, script, and resources for setting up new linux servers.',
    'long_description': README + '\n\n' +  CHANGES,
    'author': 'D\'Artagnan Palmer',
    'author_email': 'dpalmer@othermusketeer.com',
    'url': 'https://github.com/othermusketeer/ServerStarter',
    'license' : 'MIT License',
    'download_url': 'https://github.com/othermusketeer/ServerStarter/releases',
    'version': project_version,
    'packages': find_packages(),
    'scripts': ['bin/NewBox.py'],
    'install_requires': requires,
    'tests_require': requires,
    'platforms': 'any',
    'test_suite': 'ServerStarter.test.serverstarter_tests',
    'name': 'ServerStarter',
    'zip_safe': False,
    'namespace_packages': ['othermusketeer']
}

classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
        ]
        
classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Operating System :: OS Independent'
    ]
config['classifiers'] = classifiers

setup(**config)