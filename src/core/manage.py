import subprocess  # nosec

import click

from src.core import server


@click.group("Fast-api App manager")
def manage() -> None:
    # the main group of commands
    pass


@manage.command(help="Run the web server")
def run_server() -> None:
    click.echo("-> Runnning the server")
    server.run()


@manage.group(help="Manage the database")
def database() -> None:
    # group to manage data base
    pass


@database.command(help="create database")
def create() -> int:
    return subprocess.call(["alembic", "upgrade", "head"])  # nosec


@database.command(help="Make migration")
def migration(msg: str) -> int:
    return subprocess.call(["alembic", "revision", "--autogenerate", "-m", f"{msg}"])  # nosec


@database.command(help="apply migration")
def migrate() -> int:
    return subprocess.call(["alembic", "upgrade", "head"])  # nosec


if __name__ == "__main__":
    manage()
