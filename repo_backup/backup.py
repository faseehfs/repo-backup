import subprocess
import click
import sys
from . import utils


def from_repo_name(config, name: str):
    url = utils.url_from_name(config, name)
    path = utils.path_from_name(config, name)

    try:
        subprocess.run(["git", "clone", "--mirror", url, path], check=True)
    except:
        click.echo(f"Failed to clone '{name}'.")
        sys.exit(1)
