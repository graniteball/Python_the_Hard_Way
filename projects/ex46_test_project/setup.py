try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Test project for exercise 46',
	'author': 'Alan Gilbert',
	'url': 'URL to get at it.',
	'download_url': 'Where to download it.',
	'author_email': 'projects@graniteball.com',
	'version': '0.1',
	'install requires': ['nose'],
	'packages': ['ex46_test_project'],
	'scripts': [],
	'name': 'ex46_test_project'
}

setup(**config)