from setuptools import setup, find_packages

setup(
    name='limox common',
    version='0.0.1',
    author='Bifer Team',
    description='Limox common module',
    platforms='Linux',
    packages=find_packages(exclude=['tests', 'specs', 'integration_specs'])
)
