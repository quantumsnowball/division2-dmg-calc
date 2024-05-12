from dataclasses import dataclass
from division2calc.build.damage.common import Profile
from division2calc.gear import Gears
import division2calc.gear.talents as talents
import division2calc.gear.gearsets as gearsets
import division2calc.gear.gearsets.bonus as gearsets_bonus


@dataclass
class X2(Profile[float]):
    _gears: Gears

    @property
    def basic(self) -> float:
        return 1.0

    @property
    def min(self) -> float:
        return 1.0

    @property
    def average(self) -> float:
        x = 1.0
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
    def max(self) -> float:
        x = 1.0
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
