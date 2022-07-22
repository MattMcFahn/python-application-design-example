setup:
	@pyenv local 3.8.12
	@poetry install
	@poetry run pre-commit install

shell:
	@poetry shell

checks: lint pre-commit test

lint:
	@echo "Running pylint"
	@poetry run pylint --rcfile pyproject.toml data_manipulator/ tests/

pre-commit:
	@poetry run pre-commit run --all-files

test:
	@echo "Running tests"
	@poetry run pytest -s -vv --junitxml=test_results/report.xml \
	--cov-report term-missing --cov=data_manipulator tests | tee \
	test_results/pytest-coverage.txt

build: poetry-build docker-build

poetry-build:
	@echo "Building wheel"
	@poetry build

docker-build:
	@echo "Building docker image"
	docker build . -t data_manipulator

run:
	@echo "Running package in docker image with env vars"
	docker run --env-file=.env data_manipulator
