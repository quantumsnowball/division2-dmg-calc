import copy

import division2calc.agent.gear.brandsets as brandsets
import division2calc.agent.gear.gearsets as gearsets
from division2calc.agent.gear import Gears


#
# helpers
#
def enable_brandset_bonus(gears: Gears) -> None:
    # collect brandset bonus pools
    pools: dict[str, brandsets.BonusPool] = {}
    for gear in gears:
        if isinstance(gear, brandsets.Brandsets):
            id = gear.brandset
            pools[id] = gear.bonus_pool
    # assign brandset bonus to corresponding gear
    counter: dict[str, int] = {}
    for gear in gears:
        if isinstance(gear, brandsets.Brandsets):
            id = gear.brandset
            try:
                counter[id] += 1
            except KeyError:
                counter[id] = 0
            try:
                # ensure new copy of bonus object
                gear.brandset_bonus = copy.deepcopy(pools[id][counter[id]])
            except IndexError:
                pass


def enable_gearset_bonus(gears: Gears) -> None:
    # collect gearset bonus pools
    pools: dict[str, gearsets.BonusPool] = {}
    for gear in gears:
        if isinstance(gear, gearsets.Gearsets):
            id = gear.gearset
            pools[id] = gear.bonus_pool
    # assign gearset bonus to corresponding gear
    counter: dict[str, int] = {}
    for gear in gears:
        if isinstance(gear, gearsets.Gearsets):
            id = gear.gearset
            try:
                counter[id] += 1
            except KeyError:
                counter[id] = 0
            try:
                # ensure new copy of bonus object
                gear.gearset_bonus = copy.deepcopy(pools[id][counter[id]])

                # any gearsets self modification
                gear.upgrade_bonus_talent()
            except IndexError:
                pass
