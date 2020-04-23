#! /usr/bin/env sh

set -x

flake8 src/ tests/

mypy src/ tests/
