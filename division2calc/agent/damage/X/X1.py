from dataclasses import dataclass

import division2calc.agent.weapon.talents as talents
from division2calc.agent.damage.common import Profile
from division2calc.agent.stats import Stats
from division2calc.agent.weapon import Weapon


@dataclass
class X1(Profile[float]):
    _stats: Stats
    _weapon: Weapon

    @property
    def basic(self) -> float:
        x = 1.0
        # weapon damage
        x += self._stats.weapon_damage
        # weapon type damage
        x += self._stats.weapon_type_damage
        # result
        return x

    @property
    def min(self) -> float:
        x = self.basic
        # result
        return x

    @property
    def average(self) -> float:
        x = self.basic
        # weapon talent average
        if isinstance(self._weapon.talent, talents.PerfectOptimist):
            x += self._weapon.talent.max_buff * self._weapon.talent.prob
        # result
        return x

    @property
    def max(self) -> float:
        x = self.basic
        # weapon talent
        if isinstance(self._weapon.talent, talents.PerfectOptimist):
            x += self._weapon.talent.max_buff
        # result
        return x
