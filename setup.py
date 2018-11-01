import os
import pip
from setuptools import setup, find_packages



readme = 'README.md'
requirements = ['pandas>=0.23', 'scikit-learn>=0.19', 'click>=6.7']

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mallen_grubhub_test",
    version = "1.0.12",
    author = "Brenton Mallen",
    author_email = "brentonmallen1@gmail.com",
    description = ("A small module to train and save a classifier."),
    license = "MIT",
    keywords = "model train save",
    url = "https://github.com/brentonmallen1/grubhub_test",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'train = grubhub.train:main'
        ]},
    long_description=read(readme),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6"
    ],
)