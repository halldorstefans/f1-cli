from setuptools import setup

VERSION = "0.1.0"

DEPENDENCIES = [
        'click~=8.0',
        'requests~=2.25',
        'tabulate~=0.8',
    ]

setup(
    name='formula-1-cli',
    version=VERSION,
    description='Formula 1 Command-Line Tools',
    license='MIT',
    author='Halldor Stefansson',
    author_email='halldor@halldorstefans.com',
    py_modules = ['f1'],
    install_requires=DEPENDENCIES,
    entry_points='''
        [console_scripts]
        f1=f1:cli
    ''',
)