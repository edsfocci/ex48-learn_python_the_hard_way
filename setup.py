from setuptools import setup


config = {
    'description':      'My Project',
    'author':           'Ed Solis',
    'url':              'URL to get at it.',
    'download_url':     'Where to download it.',
    'author_email':     'edsfocci@gmail.com',
    'version':          '0.0.1',
    'install_requires': ['nose'],
    'packages':         ['ex48'],
    'scripts':          [],
    'name':             'projectname'
}

setup(**config)
