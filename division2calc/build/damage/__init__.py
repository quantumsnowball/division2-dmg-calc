from dataclasses import dataclass

from division2calc.build.common import Profile
from division2calc.build.stats import Stats
from division2calc.gear import Gears
from division2calc.weapon import Weapon
import division2calc.build.damage.common as common

from division2calc.build.damage.X import X
from division2calc.build.damage.Dydx import Dydx


@dataclass
class Damage(common.Profile[float]):
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
        dmg *= self.x[1].basic
        # result
        return dmg

    @property
    def min(self) -> float:
        dmg = self._weapon.base_damage
        for i in range(1, 9):
            dmg *= self.x[i].min
        return dmg

    @property
    def average(self) -> float:
        dmg = self._weapon.base_damage
        for i in range(1, 9):
            dmg *= self.x[i].average
        return dmg

    @property
    def max(self) -> float:
        dmg = self._weapon.base_damage
        for i in range(1, 9):
            dmg *= self.x[i].max
        return dmg

    def total_damage(self,
                     profile: Profile,
                     *,
                     critical: bool = False,
                     headshot: bool = False,
                     expcrit: bool = False,
                     armor: bool = False):
        # base
        dmg = self.basic
        if profile == 'basic':
            return dmg
        dmg *= getattr(self.x[2], profile)
        dmg *= getattr(self.x[3], profile)
        dmg *= getattr(self.x[4], profile)
        dmg *= getattr(self.x[5], profile)
        dmg *= self.x.x6(critical, headshot, expcrit)
        dmg *= self.x.x7(armor)
        dmg *= getattr(self.x[8], profile)
        # result
        return dmg
