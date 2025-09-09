import click

@click.group()
def cli():
    """Repository manager CLI"""
    pass

@cli.command()
@click.argument('arg')
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
