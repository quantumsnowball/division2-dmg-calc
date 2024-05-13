from dataclasses import dataclass

from division2calc.agent.damage.common import Profile
from division2calc.agent.stats import Stats


@dataclass
class X6(Profile[float]):
    _stats: Stats

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
        # weight by critical hit chance
        x += self._stats.critical_hit_chance*self._stats.critical_hit_damage
        # result
        return x

    @property
    def max(self) -> float:
        x = 1.0
        # assuming critical headshot
        x += self._stats.critical_hit_damage
        x += self._stats.headshot_damage
        # result
        return x
