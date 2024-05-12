from dataclasses import dataclass

from division2calc.build.damage.common import Profile
from division2calc.build.stats import Stats
from division2calc.utils import Float


@dataclass
class X1(Profile[Float]):
    _stats: Stats

    @property
    def basic(self) -> Float:
        pct = Float(1.0)
        pct += self._stats.weapon_damage
        pct += self._stats.weapon_type_damage
        return pct

    @property
    def min(self) -> Float:
        return self.basic

    @property
    def average(self) -> Float:
        return self.basic

    @property
    def max(self) -> Float:
        return self.basic
