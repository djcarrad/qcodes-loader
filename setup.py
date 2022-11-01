from setuptools import setup, find_packages
from distutils.version import StrictVersion
from importlib import import_module
import re


def get_version(verbose=1):
    """ Extract version information from source code """

    try:
        with open('version.py', 'r') as f:
            ln = f.readline()
            # print(ln)
            m = re.search('.* ''(.*)''', ln)
            version = (m.group(1)).strip('\'')
    except Exception as E:
        print(E)
        version = 'none'
    if verbose:
        print('get_version: %s' % version)
    return version


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='qcodesloader',
      version=get_version(),
      use_2to3=False,

      maintainer='Damon Carrad',
      maintainer_email='damonc@dtu.dk',
      description='Load data generated with qcodes=<0.1.11 or qcodes-elab',
      long_description=readme(),
      url='https://github.com/djcarrad/qcodes-loader',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering'
      ],
      license='MIT',
      # if we want to install without tests:
      # packages=find_packages(exclude=["*.tests", "tests"]),
      packages=find_packages(),

      install_requires=[
          'numpy>=1.10',
          'h5py>=2.6',
          'jupyter',
          'jsonschema',
      ],


      zip_safe=False)
