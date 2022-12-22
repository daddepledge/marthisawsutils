from setuptools import setup
import os

lib_folder = os.path.dirname(os.path.realpath(__file__))

requirement_path = lib_folder + '/requirements.txt'

install_requires = []

if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(
    name='mtawsutils',
    url='https://github.com/daddepledge/marthisawsutils.git',
    author='Sefton de Pledge',
    author_email='seftontycho@hotmail.co.uk',
    packages=['mtawsutils'],
    install_requires=install_requires,
    version='0.1',
    license='MIT',
    description='Usefull code for sending payloads and hadling databse stuff',
)