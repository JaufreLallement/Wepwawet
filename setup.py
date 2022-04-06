from setuptools import find_packages, setup
from os.path import abspath, dirname, join

from wepwawet import __version__

this_dir = abspath(dirname(__file__))

with open(join(this_dir, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

with open(join(this_dir, 'requirements.txt'), encoding='utf-8') as f:
  reqs = f.read().splitlines()

setup(
  name='wepwawet',
  version=__version__,
  description='URLs information gathering',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/JaufreLallement/Wepwawet',
  author='Jaufré Lallement',
  author_email='lallement.j.pro@outlook.fr',
  classifiers=['Intended Audience :: Developers',
                'Topic :: Utilities',
                'License :: Public Domain',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 3.10', ],
  keywords='cli',
  packages=find_packages(exclude=['docs', 'tests*']),
  install_requires=[reqs],
  entry_points={'console_scripts': ['wepwawet=wepwawet.cli:main', ], },
)