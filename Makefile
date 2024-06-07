install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py
	
lint:
	pylint --disable=R,C *.py

.PHONY: test	
test:
	python -m pytest -vv test/*.py
	
all: install lint test