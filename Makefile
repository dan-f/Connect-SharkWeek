SRC_DIRS = models

requirements:
	pip install -r requirements.txt

develop: requirements
	pip install -r dev-requirements.txt

quality:
	pep8 $(SRC_DIRS)
# 	TODO: pylint is failing due to broken code in master.
# 	Re-enable once the app works.
#	pylint $(SRC_DIRS)
