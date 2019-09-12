install:
	pip install -r requirements

build:
	python setup.py bdist_wheel

publish: install build
	twine upload dist/* 
