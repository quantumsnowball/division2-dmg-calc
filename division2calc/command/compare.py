from pathlib import Path

import click
import pandas as pd

from division2calc.utils import load_builds_file


@click.command()
@click.argument('file', required=True, type=click.Path())
@click.option('-i', '--indices', default=(0, 1,), type=click.Tuple([int, int]),
              help='which two builds in the list to display, e.g. -i 0 1')
@click.option('--x', is_flag=True, default=False, help='Enable x comparison')
@click.option('--damage', is_flag=True, default=False, help='Enable damage comparison')
@click.option('--dydx', is_flag=True, default=False, help='Enable dydx comparison')
def compare(file: Path,
            indices: tuple[int, int],
            damage: bool,
            x: bool,
            dydx: bool) -> None:
    builds = load_builds_file(file)
    build1, build2 = tuple(builds[i] for i in indices)
    all = not any((x, damage, dydx))
    if all or damage:
        click.secho(f'\ndiff(damage): Build({build2.name}) net Build({build1.name})', fg='yellow')
        diff: pd.DataFrame = build2.summary.damage - build1.summary.damage
        print(diff.round(2))
        click.secho(f'\ndiff%(damage): Build({build2.name}) net Build({build1.name})', fg='yellow')
        diffpct: pd.DataFrame = (build2.summary.damage / build1.summary.damage - 1)*100
        print(diffpct.round(4))
    if all or x:
        click.secho(f'\ndiff(x): Build({build2.name}) net Build({build1.name})', fg='yellow')
        diff: pd.DataFrame = build2.summary.x - build1.summary.x
        print(diff.round(4))
    if all or dydx:
        click.secho(f'\ndiff(dydx): Build({build2.name}) net Build({build1.name})', fg='yellow')
        diff: pd.DataFrame = build2.summary.dydx - build1.summary.dydx
        print(diff.round(4))
