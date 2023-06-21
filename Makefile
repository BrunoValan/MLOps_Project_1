install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=cli tests

format:
	black *.py


lint:
	pylint --disable=R,C cli.py
	


all: install lint test
