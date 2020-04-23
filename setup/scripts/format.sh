#! /usr/bin/env sh
set -x

autoflake --remove-all-unused-imports --remove-unused-variables  --recursive --in-place src/ tests/

black src tests

isort --recursive --apply src tests