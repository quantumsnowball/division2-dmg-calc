from dataclasses import dataclass

import division2calc.agent.gear.gearsets as gearsets
import division2calc.agent.gear.gearsets.bonus as gearsets_bonus
import division2calc.agent.gear.talents as talents
import division2calc.agent.weapon.talents as weapon_talents
from division2calc.agent.damage.common import Profile
from division2calc.agent.gear import Gears
from division2calc.agent.weapon import Weapon


@dataclass
class X2(Profile[float]):
    _weapon: Weapon
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
        # weapon
        if isinstance(self._weapon.talent, weapon_talents.Measured):
            x += +self._weapon.talent.bottom_twd_inc*(1-self._weapon.talent.prob)
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
        # weapon
        if isinstance(self._weapon.talent, weapon_talents.Measured):
            x += +self._weapon.talent.bottom_twd_inc
        # result
        return x
