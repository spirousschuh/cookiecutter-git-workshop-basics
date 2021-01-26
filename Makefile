test_default_package:
	rm -rf git_workshop_basic
	cookiecutter --no-input --directory $(shell pwd) git_workshop_basic
	# needs to be in one line otherwise the working directory does not change
	cd git_workshop_basic; pip install -e . ; tox --recreate
