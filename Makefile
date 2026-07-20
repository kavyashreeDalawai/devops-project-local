.PHONY: install db run test lint

install:
	pip install --upgrade pip
	pip install -r requirements.txt

db:
	docker run -d --name postgresql -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres -p 5432:5432 postgres:15-alpine

run:
	flask run --host=0.0.0.0 --port=5000

test:
	pynose

lint:
	flake8 .
