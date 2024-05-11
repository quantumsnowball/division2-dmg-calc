from pathlib import Path

import click

from division2calc.utils import load_builds_file


@click.command()
@click.argument('file', required=True, type=click.Path())
@click.option('-i', '--index', type=int, default=0, help='which build in the list to display')
@click.option('--stats', is_flag=True, default=False, help='Enable stats summary')
@click.option('--x', is_flag=True, default=False, help='Enable x summary')
@click.option('--damage', is_flag=True, default=False, help='Enable damage summary')
@click.option('--dydx', is_flag=True, default=False, help='Enable dydx summary')
def summary(file: Path,
            index: int,
            stats: bool,
            damage: bool,
            x: bool,
            dydx: bool) -> None:
    build = load_builds_file(file)[index]
    all = not any((stats, x, damage, dydx))
    if all or stats:
        click.secho(f'\nstats: Build({build.name})', fg='yellow')
        print(build.summary.stats)

    if all or damage:
        click.secho(f'\ndamage: Build({build.name})', fg='yellow')
        print(build.summary.damage.round(2))
    if all or x:
        click.secho(f'\nx: Build({build.name})', fg='yellow')
        print(build.summary.x.round(4))
    if all or dydx:
        click.secho(f'\ndydx: Build({build.name})', fg='yellow')
        print(build.summary.dydx.round(4))
    # pprint.pp(dataclass_asdict(build))
    # print(build_as_yaml(build))
    # pprint.pp(build)
    # print(pformat_dataclass(build))
