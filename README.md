![Build](https://github.com/slimovich/fastapi-gino-postgresql-template/workflows/Build/badge.svg)

*Under developement, WIP. Be patient.*

Overview
----------
This repository contains a skeleton app which can be used to speed-up your next project.

- **Fast-API:** Application with gino, async ORM
- **hexagonal architecture:** Bettre code organisation
- **Pipenv:** Package manager (Also creating virtual environement)
- **inject:** Python library for Dependencies injection
- **JWT:** Token authentication.
- **Gino:** Async ORM used with AsyncPG and postgreSQL
- **Alembic:** Database migrations
- **PGAdmin4:** Client for postgreSQL
- **Makefile:** Building project
- **SonarQube:** Analysing code and interpreting pytest and cov report
- **Flake8, Mypy:** Lint code
- **Isort, Black, Autoflake:** Formating code
- **Bandit:** Check for vulnerabilities   
- **Docker:** Packaging and deployment
- **Jenkins:** CI/CD

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

Sonar Qube
----------------------
TODO

Jenkins
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

Contributing
-------------
Contributions, issues and feature requests are welcome!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/YourFeature)
3. Commit your Changes (git commit -m 'Add My Feature')
4. Push to the Branch (git push origin feature/YourFeature)
5. Open a Pull Request

Contact
-----------------
* Mail: slim.baccar91@gmail.com

Release Notes
-----------------
TODO