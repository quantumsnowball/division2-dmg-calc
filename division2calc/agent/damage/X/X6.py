from dataclasses import dataclass

import division2calc.agent.weapon.talents as weapon_talents
from division2calc.agent.damage.common import Profile
from division2calc.agent.stats import Stats
from division2calc.agent.weapon import Weapon


@dataclass
class X6(Profile[float]):
    _stats: Stats
    _weapon: Weapon

    def __call__(self, critical: bool, headshot: bool, expcrit: bool) -> float:
        x = 1
        if critical:
            chd = self._stats.critical_hit_damage
            if expcrit:
                chd *= self._stats.critical_hit_chance
            x += chd
        if headshot:
            x += self._stats.headshot_damage
        # result
        return x

    @property
    def basic(self) -> float:
        return 1.0

    @property
    def min(self) -> float:
        return self.basic

    @property
    def average(self) -> float:
        x = 1.0
        chd = self._stats.critical_hit_damage
        # weapon talent
        if isinstance(self._weapon.talent, weapon_talents.Strained):
            chd += self._weapon.talent.average_buff
            # weight by critical hit chance
        x += self._stats.critical_hit_chance*chd
        # result
        return x

    @property
    def max(self) -> float:
        x = 1.0
        chd = self._stats.critical_hit_damage
        # weapon talent
        if isinstance(self._weapon.talent, weapon_talents.Strained):
            chd += self._weapon.talent.max_buff
        # assuming critical headshot
        x += chd
        x += self._stats.headshot_damage
        # result
        return x
