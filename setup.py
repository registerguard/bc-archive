try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Brightcove video archiver',
    'author': 'Rob Denton/The Register-Guard',
    'url': 'https://github.com/registerguard/bc-archive/',
    'download_url': 'https://github.com/registerguard/bc-archive/',
    'author_email': 'rob.denton@registerguard.com',
    'version': '0.1',
    'install_requires': ['pytest','requests','requests_oauthlib'],
    'packages': [],
    'scripts': [],
    'name': 'BC-Archive'
}

setup(**config)

