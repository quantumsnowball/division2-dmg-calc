from dataclasses import dataclass
from division2calc.build.damage.common import Profile
from division2calc.build.stats import Stats


@dataclass
class X7(Profile[float]):
    _stats: Stats

    def __call__(self, armor: bool) -> float:
        x = 1.0
        if armor:
            x += self._stats.damage_to_armor
        else:
            x += self._stats.damage_to_health
        # result
        return x

    @property
    def basic(self) -> float:
        return 1.0

    @property
    def min(self) -> float:
        x = 1.0
        # assume whoever being the lowest
        x += min(self._stats.damage_to_armor, self._stats.damage_to_health)
        # result
        return x

    @property
    def average(self) -> float:
        # assuming equal chance for armor and health damage
        x = 1.0
        x += 0.5*self._stats.damage_to_armor + 0.5*self._stats.damage_to_health
        # result
        return x

    @property
    def max(self) -> float:
        x = 1.0
        # assume whoever being the highest
        x += max(self._stats.damage_to_armor, self._stats.damage_to_health)
        # result
        return x
