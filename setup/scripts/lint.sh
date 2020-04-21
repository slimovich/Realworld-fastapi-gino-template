#! /usr/bin/env sh

set -e
set -x


flake8 ../../src
mypy ../../src

black --check ../../src --diff
isort --recursive --check-only ../../src