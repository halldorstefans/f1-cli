import pathlib
from setuptools import setup

VERSION = "0.1.0"

CLASSIFIERS = [
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
        'click~=8.0',
        'requests~=2.25',
        'tabulate~=0.8',
    ]

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='formula-1-cli',
    version=VERSION,
    description='Formula 1 Command-Line Tools',
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/halldorstefans/f1-cli",
    author='Halldor Stefansson',
    author_email='halldor@halldorstefans.com',
    classifiers=CLASSIFIERS,
    py_modules = ['f1'],
    include_package_data=True,
    install_requires=DEPENDENCIES,
    entry_points='''
        [console_scripts]
        f1=f1:cli
    ''',
)