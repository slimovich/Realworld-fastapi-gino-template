#! /usr/bin/env sh

set -e
set -x


pytest --verbose --cov=src --cov=tests --cov-report=term-missing --cov-report=xml:reports/coverage.xml --junit-xml=reports/tests.xml