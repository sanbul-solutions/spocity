install:
	pip install --upgrade pip && \
		pip install -r requirements.txt
lint:
	pylint --disable=R,C api/*.py

test:
	pytest

build:
	# build container

deploy:
	# deploy

all: install lint test deploy