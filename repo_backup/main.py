from datetime import datetime

from . import backup
from . import config

import click


@click.group()
def cli():
    pass


@cli.command(name="config")
def configure():
    config.reset()


@cli.command(name="backup")
@click.argument("arg")
def backup_command(arg):
    match arg.lower():
        case "all":
            click.echo("Not currently supported.")
        case "public":
            click.echo("Not currently supported.")
        case "private":
            click.echo("Not currently supported.")
        case _:
            repo_name = arg
            backup.from_repo_name(configuration, repo_name)


if __name__ == "__main__":
    configuration = config.load()
    cli()
