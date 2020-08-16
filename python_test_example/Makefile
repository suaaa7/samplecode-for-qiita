image = unittest
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

.PHONY: all_test
all_test:
	python3 -m unittest discover --verbose --pattern "*_test.py"
