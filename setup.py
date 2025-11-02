## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import find_packages, setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    # Discover all Python subpackages under python
    packages=find_packages(where="python"),
    package_dir={"": "python"},
)

setup(**setup_args)
