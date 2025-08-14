
from setuptools import setup

setup (name = 'ugit',
       version = '0.3',
       packages = ['ugit'],
       entry_points = {
           'console_scripts' : [
               'ugit = ugit.cli:main'
               ]
            })
