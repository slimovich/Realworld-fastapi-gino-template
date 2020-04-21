#! /usr/bin/env sh
set -e

uvicorn src.core.server:app --reload --workers 1 --host 0.0.0.0 --port 8000 --log-level debug --access-log