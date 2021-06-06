import pathlib
import formula1
from setuptools import find_packages, setup

VERSION = "0.1.2"

CLASSIFIERS = [
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
        'click>=8.0',
        'requests>=2.25',
        'pandas>=1.2',
    ]

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='formula1-cli',
    version=VERSION,
    description='Formula 1 Command-Line Tools',
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/halldorstefans/f1-cli",
    author='Halldor Stefansson',
    author_email='halldor@halldorstefans.com',
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=DEPENDENCIES,
    entry_points={
        'console_scripts': [
        'f1=formula1.f1:cli',
        ]
    },
)