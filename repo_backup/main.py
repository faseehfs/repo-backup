import click
import json


CONFIG_FILE = "config.json"
DEAFAULT_CONFIG = {"backup_directory": "cwd", "lfs": False, "pat": ""}


@click.group()
def cli():
    pass


@cli.command()
def config():
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(DEAFAULT_CONFIG, f, indent=4)


@cli.command()
@click.argument("arg")
def backup(arg):
    if arg == "all":
        click.echo("Not currently supported.")
    elif arg == "public":
        click.echo("Not currently supported.")
    elif arg == "private":
        click.echo("Not currently supported.")
    else:
        click.echo(f"backing up {arg}")


@cli.command()
def status():
    click.echo("Not currently supported.")


if __name__ == "__main__":
    cli()
