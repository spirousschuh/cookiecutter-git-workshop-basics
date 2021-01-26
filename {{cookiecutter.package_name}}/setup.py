import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="{{cookiecutter.package_name}}",
    version="0.0.1",
    url="{{cookiecutter.package_url}}",
    license='MIT',

    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",

    description="{{cookiecutter.package_description}}",
    long_description=read("README.md"),
    packages=find_packages(exclude=('tests',)),
    install_requires=['click', 'matplotlib', 'Pillow'],
    entry_points = {
        'console_scripts': ['image_magic={{cookiecutter.package_name}}.cli:cli_group'],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
