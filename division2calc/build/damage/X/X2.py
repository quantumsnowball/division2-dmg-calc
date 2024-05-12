from dataclasses import dataclass

import division2calc.gear.gearsets as gearsets
import division2calc.gear.gearsets.bonus as gearsets_bonus
import division2calc.gear.talents as talents
from division2calc.build.damage.common import Profile
from division2calc.gear import Gears
from division2calc.utils import Float


@dataclass
class X2(Profile[Float]):
    _gears: Gears

    @property
    def basic(self) -> Float:
        return Float(1.0)

    @property
    def min(self) -> Float:
        return Float(1.0)

    @property
    def average(self) -> Float:
        x = Float(1.0)
        # backpack
        # chest
        if isinstance(self._gears.chest.talent, talents.Obliterate):
            x += self._gears.chest.talent.average
        # gearset
        for gear in self._gears:
            if isinstance(gear, gearsets.Gearsets):
                if isinstance(gear.gearset_bonus, gearsets_bonus.StrikersGamble):
                    x += gear.gearset_bonus.average
        # result
        return x

    @property
    def max(self) -> Float:
        x = Float(1.0)
        # backpack
        # chest
        if isinstance(self._gears.chest.talent, talents.Obliterate):
            x += self._gears.chest.talent.max
        # gearset
        for gear in self._gears:
            if isinstance(gear, gearsets.Gearsets):
                if isinstance(gear.gearset_bonus, gearsets_bonus.StrikersGamble):
                    x += gear.gearset_bonus.max
        # result
        return x
