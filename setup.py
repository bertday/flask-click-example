from setuptools import setup, find_packages

setup(
    name='flask-cli',
    version='0.1',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        ais = ais.cli:cli
    '''
)
