from setuptools import setup, find_packages

setup(
    name='adagio common',
    version='0.0.1',
    author='Bifer Team',
    description='Adagio common module',
    platforms='Linux',
    packages=find_packages(exclude=['tests', 'specs', 'integration_specs'])
)
