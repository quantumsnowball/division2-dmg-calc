from dataclasses import dataclass

from division2calc.build.damage.common import Profile
from division2calc.build.stats import Stats
from division2calc.utils import Float


@dataclass
class X7(Profile[Float]):
    _stats: Stats

    def __call__(self, armor: bool) -> Float:
        x = Float(1.0)
        if armor:
            x += self._stats.damage_to_armor
        else:
            x += self._stats.damage_to_health
        # result
        return x

    @property
    def basic(self) -> Float:
        return Float(1.0)

    @property
    def min(self) -> Float:
        x = Float(1.0)
        # assume whoever being the lowest
        # TODO
        x += min(self._stats.damage_to_armor, self._stats.damage_to_health)
        # result
        return x

    @property
    def average(self) -> Float:
        # assuming equal chance for armor and health damage
        x = Float(1.0)
        # TODO
        x += 0.5*self._stats.damage_to_armor + 0.5*self._stats.damage_to_health
        # result
        return x

    @property
    def max(self) -> Float:
        x = Float(1.0)
        # assume whoever being the highest
        # TODO
        x += max(self._stats.damage_to_armor, self._stats.damage_to_health)
        # result
        return x
