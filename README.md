*Under developement, WIP. Be patient.*

Overview
----------
- Fast-API application with gino, async ORM
- Using hexagonal architecture
- Pipenv for package manager (Also creating virtual environement)
- Dependencies injection using ``inject`` library
- PostgreSQL as a databse
- PGAdmin4 client for postgreSQL
- Makefile for building project
- SonarCube for analysing code and interpreting pytest and cov report
- Docker for packaging and deployment
- Flake8 and Mypy for analysing code
- Isort, Black, Autoflake for formating code
- Jenkins for CI/CD

Quickstart
----------
for running the server locally
- first install pipenv
```bash
pip install pipenv
```
- install the dependencies locally
```bash
PIPENV_DOTENV_LOCATION=local.env pipenv run make install-dev-deps
```
- run unit test
```bash
PIPENV_DOTENV_LOCATION=local.env pipenv run make test
```
- run the local server with localhost:8080
```bash
PIPENV_DOTENV_LOCATION=local.env pipenv run make run
```

Deployment with Docker
----------------------
TODO


Project structure
-----------------

Files related to application are in the ``src`` or ``tests`` directories.
Application parts are:

    src
    ├── api                     - web related stuff.
    ├── core                    - application configuration, server management, logging.
    ├── domain                  - Business logic.
    ├── infrastructure          - external services of the application like db.
    └── main.py                 - FastAPI application entry point.