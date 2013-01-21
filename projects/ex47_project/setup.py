try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Exercise 47',
	'author': 'Alan Gilbert',
	'url': 'URL to get at it.'
	'download_url': 'Where to download it.',
	'author_email': 'projects@graniteball.com',
	'version': '0.1',
	'install requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'Exercise 47'
}

setup(**config)