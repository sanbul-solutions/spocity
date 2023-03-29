install:
	pip install --upgrade pip && \
		pip install -r requirements.txt
lint:
	pylint --disable=R,C api/*.py

test:
	pytest tests

build:
	docker build -t streaming .

run:
	#docker run -p 8000:8000 streaming

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 855301726013.dkr.ecr.us-east-1.amazonaws.com
	docker build -t streaming .
	docker tag streaming:latest 855301726013.dkr.ecr.us-east-1.amazonaws.com/streaming:latest
	docker push 855301726013.dkr.ecr.us-east-1.amazonaws.com/streaming:latest

all: install lint test build run deploy