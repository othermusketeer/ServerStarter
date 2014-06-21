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
try:
	CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except:
	CHANGES = ""

requires = []
#requires=['pyramid>=1.3', 'pyramid_jinja2', 'wtforms', 'webhelpers']

config = {
    'description': 'My Project',
	'long_description': README + '\n\n' +  CHANGES,
    'author': 'D\'Artagnan Palmer',
	'author_email': 'dpalmer@othermusketeer.com',
    'url': 'URL to get it at.',
	'license' : 'MIT License',
    'download_url': 'Where to download it.',
    'version': project_version,
    'install_requires': ['nose'],
    'packages': find_packages(),
    'scripts': [],
	'install_requires': requires,
	'tests_require': requires,
	'platforms': 'any',
	'test_suite': 'NAME.test.NAME_tests',
    'name': 'projectname',
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