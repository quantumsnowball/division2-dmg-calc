from dataclasses import dataclass
from division2calc.build.damage.common import Profile
from division2calc.build.stats import Stats


@dataclass
class X1(Profile[float]):
    _stats: Stats

    @property
    def basic(self) -> float:
        return 1+self._stats.weapon_damage+self._stats.weapon_type_damage

    @property
    def min(self) -> float:
        return self.basic

    @property
    def average(self) -> float:
        return self.basic

    @property
    def max(self) -> float:
        return self.basic
