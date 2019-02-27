from distutils.core import setup
import os, sys

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

setup(name='visa',
      version='1.0.0',
      description='Visa python bindings',
      author='Hprobotic',
      author_email='hprobotic@gmail.co ',
      url='https://nomadzy.com/',
      packages=['visa'],
      requires=['json', 'pycurl']
)