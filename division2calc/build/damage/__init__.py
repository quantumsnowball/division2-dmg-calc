from dataclasses import dataclass

from build.stats import Stats
from gear import Gears
from weapon import Weapon

from build.damage.X import X
from build.damage.Dydx import Dydx


@dataclass
class Damage:
    _weapon: Weapon
    _gears: Gears
    _stats: Stats

    def __post_init__(self) -> None:
        self.x = X(self._weapon, self._gears, self._stats)
        self.dydx = Dydx(self.x)

    @property
    def basic(self) -> float:
        # base
        dmg = self._weapon.base_damage
        # basic weapon damage
        dmg *= self.x.x1
        # result
        return dmg

    @property
    def min(self) -> float:
        dmg = self.basic
        dmg *= self.x.x2_min
        dmg *= self.x.x6_min
        dmg *= self.x.x7_min
        dmg *= self.x.x8
        # result
        return dmg

    @property
    def average(self) -> float:
        dmg = self.basic
        dmg *= self.x.x2_mean
        dmg *= self.x.x6_mean
        dmg *= self.x.x7_mean
        dmg *= self.x.x8
        # result
        return dmg

    @property
    def max(self) -> float:
        dmg = self.basic
        dmg *= self.x.x2_max
        dmg *= self.x.x6_max
        dmg *= self.x.x7_max
        dmg *= self.x.x8
        # result
        return dmg

    def total_damage(self,
                     *,
                     critical: bool = False,
                     headshot: bool = False,
                     armor: bool = False):
        # base
        dmg = self._weapon.base_damage
        dmg *= self.x.x1
        dmg *= self.x.x2
        dmg *= self.x.x6(critical, headshot)
        dmg *= self.x.x7(armor)
        dmg *= self.x.x8
        # result
        return dmg
