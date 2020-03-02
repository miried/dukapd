from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dkpd',
    version='0.1.0',
    description='',
    long_description=readme,
    author='Michael Rieder',
    author_email='rieder@physik.uzh.ch',
    url='https://github.com/miried/dkpd',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
