import click
import json
import os
import sys


CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "github_username": "",
    "backup_directory": "",
    "lfs": False,
    "pat": "",
}


def reset():
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)


def load():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        reset()
        click.echo("Created config.json.")
        sys.exit(0)
