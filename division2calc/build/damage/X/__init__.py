from dataclasses import dataclass
from typing import Literal

from division2calc.build.damage.X.X1 import X1
from division2calc.build.damage.X.X2 import X2
from division2calc.build.damage.common import Profile
from division2calc.build.stats import Stats
from division2calc.gear import Gears
from division2calc.weapon import Weapon


Name = Literal['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
X_Value = dict[Name, float]


@dataclass
class X(Profile[X_Value]):
    _weapon: Weapon
    _gears: Gears
    _stats: Stats

    '''
    Total Damage =
    Base weapon Damage
    x1|    *(1+Weapon Damage+Weapon Type Damage+Weapon Damage Talents)
    x2|    *(1+Total Weapon Damage Talents) [Vigilance]
    x3|    *(1+Amplfied Talent 1)
    x4|    *(1+Amplfied Talent 2)
    x5|    *(1+Amplfied Talent 3)
    x6|    *(1+Critical Hit Damage+Headshot Damage)
    x7|    *(1+Damage to Armor+Damage to Health)
    x8|    *(1+Damage out of Cover)
    '''

    def __post_init__(self) -> None:
        self.x1 = X1(self._stats)
        self.x2 = X2(self._gears)

    #
    # x3
    #

    @property
    def x3(self) -> float:
        # TODO
        return 1.0
    #
    # x4
    #

    @property
    def x4(self) -> float:
        # TODO
        return 1.0
    #
    # x5
    #

    @property
    def x5(self) -> float:
        # TODO
        return 1.0
    #
    # x6
    #

    def x6(self, critical: bool, headshot: bool, expcrit: bool) -> float:
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
    def x6_min(self) -> float:
        return 1.0

    @property
    def x6_average(self) -> float:
        x = 1.0
        # weight by critical hit chance
        x += self._stats.critical_hit_chance*self._stats.critical_hit_damage
        # result
        return x

    @property
    def x6_max(self) -> float:
        x = 1.0
        # assuming critical headshot
        x += self._stats.critical_hit_damage
        x += self._stats.headshot_damage
        # result
        return x

    #
    # x7
    #
    def x7(self, armor: bool) -> float:
        x = 1.0
        if armor:
            x += self._stats.damage_to_armor
        else:
            x += self._stats.damage_to_health
        # result
        return x

    @property
    def x7_min(self) -> float:
        x = 1.0
        # assume whoever being the lowest
        x += min(self._stats.damage_to_armor, self._stats.damage_to_health)
        # result
        return x

    @property
    def x7_average(self) -> float:
        # assuming equal chance for armor and health damage
        x = 1.0
        x += 0.5*self._stats.damage_to_armor + 0.5*self._stats.damage_to_health
        # result
        return x

    @property
    def x7_max(self) -> float:
        x = 1.0
        # assume whoever being the highest
        x += max(self._stats.damage_to_armor, self._stats.damage_to_health)
        # result
        return x

    #
    # x8
    #
    @property
    def x8(self) -> float:
        x = 1.0
        x += self._stats.damage_to_target_out_of_cover
        # result
        return x

    #
    # use cases
    #
    @property
    def basic(self) -> X_Value:
        return {'x1': self.x1.basic,
                'x2': self.x2.basic,
                'x3': 1.0,
                'x4': 1.0,
                'x5': 1.0,
                'x6': 1.0,
                'x7': 1.0,
                'x8': self.x8}

    @property
    def min(self) -> X_Value:
        return {'x1': self.x1.min,
                'x2': self.x2.min,
                'x3': self.x3,
                'x4': self.x4,
                'x5': self.x5,
                'x6': self.x6_min,
                'x7': self.x7_min,
                'x8': self.x8}

    @property
    def average(self) -> X_Value:
        return {'x1': self.x1.average,
                'x2': self.x2.average,
                'x3': self.x3,
                'x4': self.x4,
                'x5': self.x5,
                'x6': self.x6_average,
                'x7': self.x7_average,
                'x8': self.x8}

    @property
    def max(self) -> X_Value:
        return {'x1': self.x1.max,
                'x2': self.x2.max,
                'x3': self.x3,
                'x4': self.x4,
                'x5': self.x5,
                'x6': self.x6_max,
                'x7': self.x7_max,
                'x8': self.x8}
