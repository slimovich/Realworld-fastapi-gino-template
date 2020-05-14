
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
	@echo "  check-vul                   check vulnerabilities"
	@echo "  run-local                   run the server in localhost with debug and autoreload mode"
	@echo "  run                         run the server in the container"

.PHONY: install-dev-deps
install-dev-deps:
	pipenv install --dev

.PHONY: build-dev
build-dev:
	@echo "###################################"
	@echo "# Building development image"
	docker-compose -f setup/docker/docker-compose.develop.yml build

.PHONY: build-prod
build-prod:
	@echo "###################################"
	@echo "# Building production image"
	docker-compose -f setup/docker/docker-compose.production.yml build

.PHONY: run-dev-containers
run-dev-containers:
	@echo "###################################"
	@echo "# Running development containers"
	docker-compose -f setup/docker/docker-compose.develop.yml up

.PHONY: run-prod-containers
run-prod-containers:
	@echo "###################################"
	@echo "# Running production containers"
	docker-compose -f setup/docker/docker-compose.production.yml up

.PHONY: test
test:
	@echo "###################################"
	@echo "# Running unittest"
	pytest --verbose --cov=src --cov=tests --cov-report=term-missing --cov-report=xml:reports/coverage.xml --junit-xml=reports/tests.xml

.PHONY: lint
lint:
	@echo "###################################"
	@echo "# Lint the python code"
	@[ -f ./reports/flake8.txt ] || (rm ./reports/flake8.txt)
	flake8 src/ tests/
	mypy src/ tests/

.PHONY: format
format:
	@echo "###################################"
	@echo "# Format the python code"
	autoflake --remove-all-unused-imports --remove-unused-variables  --recursive --in-place src/ tests/
	black --line-length 100 src tests
	isort --recursive --apply src tests

.PHONY: check-vul
check-vul:
	@echo "###################################"
	@echo "# Check vulnerabilities"
	bandit -r src/

.PHONY: run-dev
run-dev:
	@echo "###################################"
	@echo "# Running dev server"
	uvicorn src.core.server:app --reload --lifespan on --workers 1 --host 0.0.0.0 --port 8080 --log-level debug

.PHONY: run
run:
	@echo "###################################"
	@echo "# Running server"
	uvicorn src.core.server:app --lifespan on --workers 1 --host 0.0.0.0 --port 8080