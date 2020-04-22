*Under developement, WIP. Be patient.*

Quickstart
----------
TODO

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