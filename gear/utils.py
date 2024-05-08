import gear.brandsets as brandsets
import gear.gearsets as gearsets
from gear import Gear


#
# helpers
#
def enable_brandset_bonus(gears: tuple[Gear, ...]) -> None:
    pools: dict[str, brandsets.BonusPool] = {}
    for gear in gears:
        if isinstance(gear, brandsets.Brandsets):
            id = gear.brandset
            pools[id] = gear.bonus_pool
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


def enable_gearset_bonus(gears: tuple[Gear, ...]) -> None:
    pools: dict[str, gearsets.BonusPool] = {}
    for gear in gears:
        if isinstance(gear, gearsets.Gearsets):
            id = gear.gearset
            pools[id] = gear.bonus_pool
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
            except IndexError:
                pass
