from pathlib import Path

import click

from division2calc.utils import load_builds_file, pformat_dataclass


@click.command()
@click.argument('file', required=True, type=click.Path())
@click.option('-i', '--index', type=int, default=0, help='which build in the list to display')
def summary(file: Path,
            index: int) -> None:
    build = load_builds_file(file)[index]
    # pprint.pp(dataclass_asdict(build))
    # print(build_as_yaml(build))
    print(pformat_dataclass(build))
