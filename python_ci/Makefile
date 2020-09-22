image = python-ci
tag = 0.1.0
curdir := `pwd`

.PHONY: dbuild
dbuild:
	docker build -t $(image):$(tag) .

.PHONY: drun
drun:
	docker run --rm -it -v $(curdir):/opt -w /opt $(image):$(tag) bash

.PHONY: drmi
drmi:
	docker rmi -f $(image):$(tag)

.PHONY: flake8
flake8:
	flake8 --config=config/tox.ini src

.PHONY: mypy
mypy:
	mypy --config=config/mypy.ini src

.PHONY: test
test:
	python3 -m unittest discover --verbose src
