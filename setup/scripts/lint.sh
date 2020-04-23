#! /usr/bin/env sh

set -x

FILE=reports/flake8.txt
if [ -f "$FILE" ]; then
    echo "$FILE exist"
    rm reports/flake8.txt
else 
    echo "$FILE does not exist"
fi

flake8 src/ tests/

mypy src/ tests/
