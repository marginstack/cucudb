from os import path
from setuptools import setup, find_packages
from codecs import open

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="cucudb",
    version="0.0.1",
    description="A lightweight and simple database using simplejson.",
    author="Mattia Terenzi",
    author_email="m.terenzi92@gmail.com",
    url="https://github.com/marginstack/cucudb",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Database"],
    py_modules=['cucudb'],
    install_requires=['simplejson'])
