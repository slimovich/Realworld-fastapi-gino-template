> ### 🛠 Status: WIP
>
> *Under developement, WIP. Be patient.*

![Build Status](https://github.com/slimovich/fastapi-gino-postgresql-template/workflows/Build/badge.svg)
[![codecov](https://codecov.io/gh/slimovich/Realworld-fastapi-gino-template/branch/master/graph/badge.svg)](https://codecov.io/gh/slimovich/Realworld-fastapi-gino-template)

A real wolrd template project using Fastapi framework as well as a full implementation of CI/CD

Overview
----------
This repository contains a skeleton app which can be used to speed-up your next project.

- **Fast-API:** Asynchronous RESTful API Framework
- **Gino:** Async ORM used with AsyncPG and postgreSQL
- **Alembic:** Database migrations
- **hexagonal architecture:** Bettre code organisation
- **Pipenv:** Package manager (Also creating virtual environement)
- **Pytest:** Run unit test with code coverage
- **JWT:** Token authentication.
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

- setup a local environnement
```bash
source setup/scripts/setEnv.sh
```

- install the dependencies locally
```bash
pipenv run make install-dev-deps
```

The command above will install for you a separate environnement and installing all dependencies

- run unit test
```bash
pipenv run make test
```

- run the local server with localhost:8080
```bash
pipenv run make run
```

Deployment with Docker
----------------------
You must have docker and docker-compose tools installed in your system. Then just run:

```bash
make build-dev
make run-dev-containers
```

This will build the images and run 3 containers (Fastapi application, PostgreSQL, PGAdmin 4) in developement environnement.

If you want to run the containers in production environnement, you can do the following:

```bash
make build-prod
make run-prod-containers
```

Your can find the files to configure each environnement in the root directory:
- env-develop.env
- env-production.env

Application will be available on localhost in your browser.

All routes are available on /docs paths with Swagger

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