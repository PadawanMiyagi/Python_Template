try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jacob Bennedsen',
    'url': 'https://github.com/padawanMiyagi',
    'download_url': 'Where do you download this?',
    'author_email': 'Jacob@Bennedsen.dk',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['bin/test.py'],
    'name': 'ProjectName'
}

setup(**config)