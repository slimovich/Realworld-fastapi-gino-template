  
.PHONY: install-dev-deps build-dev build-prod run-dev-containers run-prod-containers help test lint format run run-local


SUPPORTED_COMMANDS := test lint format run
SUPPORTS_MAKE_ARGS := $(findstring $(firstword $(MAKECMDGOALS)), $(SUPPORTED_COMMANDS))
ifneq "$(SUPPORTS_MAKE_ARGS)" ""
  COMMAND_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(COMMAND_ARGS):;@:)
endif

help:
	@echo "  install-dev-deps            install dev dependencies"
	@echo "  build-dev                   build docker image for developement"
	@echo "  build-prod                  build docker image for production"
	@echo "  run-dev-containers          run docker containers for developement"
	@echo "  run-prod-containers         run docker containers for production"
	@echo "  test                        run the testsuite"
	@echo "  lint                        check the source for style errors"
	@echo "  format                      format the python code"
	@echo "  run-local                   run the server in localhost with debug and autoreload mode"
	@echo "  run                         run the server in the container"

install-dev-deps:
	pipenv install --dev

build-dev:
	docker-compose -f setup/docker/docker-compose.develop.yml build

build-prod:
	docker-compose -f setup/docker/docker-compose.production.yml build

run-dev-containers:
	docker-compose -f setup/docker/docker-compose.develop.yml up

run-prod-containers:
	docker-compose -f setup/docker/docker-compose.production.yml up

test:
	pytest --verbose --cov=src --cov=tests --cov-report=term-missing --cov-report=xml:reports/coverage.xml --junit-xml=reports/tests.xml

lint:
	@[ -f ./reports/flake8.txt ] || (rm ./reports/flake8.txt)
	flake8 src/ tests/
	mypy src/ tests/

format:
	autoflake --remove-all-unused-imports --remove-unused-variables  --recursive --in-place src/ tests/
	black src tests
	isort --recursive --apply src tests

run-dev:
	uvicorn src.core.server:app --reload --lifespan on --workers 1 --host 0.0.0.0 --port 8080 --log-level debug

run:
	uvicorn src.core.server:app --lifespan on --workers 1 --host 0.0.0.0 --port 8080