from dataclasses import replace

import gear.brandsets as brandsets
import gear.gearsets as gearsets
import gear.talents as talents
from gear import Gears
from gear.gearsets.bonus import StrikersGamble
from gear.gearsets.StrikersBattlegear import StrikersBattlegear


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
                gear.brandset_bonus = pools[id][counter[id]]
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
                gear.gearset_bonus = pools[id][counter[id]]

                # any gearsets self modification
                if isinstance(gear.gearset_bonus, StrikersGamble):
                    gear.gearset_bonus.upgrade_from(gears)
            except IndexError:
                pass
