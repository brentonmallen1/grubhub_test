# Model Train and Save Test
Author: [Brenton Mallen](https://www.brentonmallen.com)

This is a package to build a ML model and save it to disk.

## To Run
The CLI requires an integer argument called `--region_id`.

Example run call: `python src/train.py --region_id 1`

For CLI help type `python src/train.py -h` in the package root directory 

### Run Tests
To run tests, run the following command in the package root directory:
`make test`

## TODOs
Outside of the time constrain, there are a number of improvements:
1. Continuous integration and deployment with something like Jenkins
1. Implement mypy for type checking to reduce potential errors
1. Implement linting for quality checking
1. Explore using [tox](https://tox.readthedocs.io/en/latest/) for
platform testing
1. 