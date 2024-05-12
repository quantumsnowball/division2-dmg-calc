from dataclasses import dataclass

from division2calc.build.damage.common import Profile
from division2calc.build.stats import Stats
from division2calc.utils import Float


@dataclass
class X6(Profile[Float]):
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
    def basic(self) -> Float:
        return Float(1.0)

    @property
    def min(self) -> Float:
        return self.basic

    @property
    def average(self) -> Float:
        x = Float(1.0)
        # weight by critical hit chance
        x += self._stats.critical_hit_chance*self._stats.critical_hit_damage
        # TODO
        # result
        return x

    @property
    def max(self) -> Float:
        x = Float(1.0)
        # assuming critical headshot
        x += self._stats.critical_hit_damage
        x += self._stats.headshot_damage
        # result
        return x
