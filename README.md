# Model Train and Save Test
Author: [Brenton Mallen](https://www.brentonmallen.com)

This is a package to build a ML model and save it to disk.

## Installation
`pip install mallen_grubhub_test`

or install manually by cloning the repo and running

`python setup.py install`

## To Run
The CLI requires an integer argument called `--region_id`.

Example run call: `train --region_id 1`
(This will train a classifier on region `1`)

For CLI help type `python src/train.py -h` in the package root directory 

### Run Tests
To run tests, run the following command in the package root directory:
`make test`

### Development
Either a Conda environment using `conda env update` in the root directory
or by using virtualenv by first initializing the environment with 
`virtualenv grubhub-venv`, activating with `grubhub-venv/bin/activate` and 
installing the dependencies using `pip install -r requirements.txt`

**Updating pypi package**
Upload to pypi can be done using the `make package-test` command.
It will ask for credentials for a test pypi account.

Similarly, production can be updated using the `make package-prod` command.

For reference, see the [tutorial](https://packaging.python.org/tutorials/packaging-projects/)

## TODOs
Outside of the time constrain, there are a number of improvements:
1. Continuous integration and deployment with something like Jenkins
1. Implement mypy for type checking to reduce potential errors
1. Implement linting for quality checking
1. Explore using [tox](https://tox.readthedocs.io/en/latest/) for
platform testing