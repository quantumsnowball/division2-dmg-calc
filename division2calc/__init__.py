from pathlib import Path

import click


@click.group()
def division2calc() -> None:
    pass


@division2calc.command()
@click.argument('file', required=True, type=str)
def summary(file: str) -> None:
    print(Path(file))
