import click

import division2calc.agent.gear.attrs as gearattrs
import division2calc.agent.gear.brandsets.Lengmo as Lengmo
import division2calc.agent.gear.brandsets.OverlordArmaments as Overlord
import division2calc.agent.gear.gearsets.StrikersBattlegear as Striker
import division2calc.agent.gear.mods as gearmods
import division2calc.agent.weapon.AR as AR
import division2calc.agent.weapon.LMG as LMG
from division2calc.agent import Build
from division2calc.agent.specialization import Gunner
from division2calc.command.breakdown import breakdown
from division2calc.command.compare import compare
from division2calc.command.damage import damage
from division2calc.command.dps import dps
from division2calc.command.dydx import dydx
from division2calc.command.rank import rank
from division2calc.command.stats import stats
from division2calc.command.summary import summary
from division2calc.command.x import x

__all__ = [
    'Build',
    'Gunner',
    'AR',
    'LMG',
    'Striker',
    'Lengmo',
    'Overlord',
    'gearattrs',
    'gearmods',
]


@click.group()
def division2calc() -> None:
    pass


division2calc.add_command(stats)
division2calc.add_command(breakdown)
division2calc.add_command(damage)
division2calc.add_command(x)
division2calc.add_command(dydx)
division2calc.add_command(summary)
division2calc.add_command(dps)
division2calc.add_command(compare)
division2calc.add_command(rank)
