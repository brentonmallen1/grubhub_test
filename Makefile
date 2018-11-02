# ------------
#  TESTING
# ------------
.PHONY: test
test:
	python -m pytest -s


# -------
# Package
# -------

.PHONY: clean-dist
clean-dist:
	- rm dist/*

.PHONY: package-test
package-test: clean-dist
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: package-prod
package-prod: clean-dist
	python setup.py sdist bdist_wheel
	twine upload dist/*
