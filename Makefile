
SUPPORTED_COMMANDS := test lint format run
SUPPORTS_MAKE_ARGS := $(findstring $(firstword $(MAKECMDGOALS)), $(SUPPORTED_COMMANDS))
ifneq "$(SUPPORTS_MAKE_ARGS)" ""
  COMMAND_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(COMMAND_ARGS):;@:)
endif

help:
	@echo "  clean                       clean files"
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

.PHONY: clean
clean:
	@echo "--> Cleaning pyc files"
	find . -name "*.pyc" -delete

.PHONY: install-dev-deps
install-dev-deps:
	pipenv install --dev

.PHONY: build-dev
build-dev:
	@echo "--> Building development image"
	docker-compose -f setup/docker/docker-compose.develop.yml build

.PHONY: build-prod
build-prod:
	@echo "--> Building production image"
	docker-compose -f setup/docker/docker-compose.production.yml build

.PHONY: run-dev-containers
run-dev-containers:
	@echo "--> Running development containers"
	docker-compose -f setup/docker/docker-compose.develop.yml up

.PHONY: run-prod-containers
run-prod-containers:
	@echo "--> Running production containers"
	docker-compose -f setup/docker/docker-compose.production.yml up

.PHONY: test
test:
	@echo "--> Running unittest"
	pytest --verbose --cov=src --cov=tests --cov-report=term-missing --cov-report=xml:.artifacts/coverage.xml --junit-xml=.artifacts/tests.xml

.PHONY: lint
lint:
	@echo "--> Analyse code"
	@[ -d ./.artifacts/ ] || (rm -rf ./.artifacts/)
	mkdir ./.artifacts/
	flake8 src/ tests/
	mypy src/ tests/

.PHONY: format
format:
	@echo "--> Format the python code"
	autoflake --remove-all-unused-imports --remove-unused-variables  --recursive --in-place src/ tests/
	black --line-length 100 src tests
	isort --recursive --apply src tests

.PHONY: check-vul
check-vul:
	@echo "--> Check vulnerabilities"
	bandit -r src/

.PHONY: run-dev
run-dev:
	@echo "--> Running dev server"
	uvicorn src.core.server:app --reload --lifespan on --workers 1 --host 0.0.0.0 --port 8080 --log-level debug

.PHONY: run
run:
	@echo "--> Running server"
	uvicorn src.core.server:app --lifespan on --workers 1 --host 0.0.0.0 --port 8080