from dataclasses import dataclass
from typing import Literal

from division2calc.build.damage.X.X1 import X1
from division2calc.build.damage.X.X2 import X2
from division2calc.build.damage.X.X3 import X3
from division2calc.build.damage.X.X4 import X4
from division2calc.build.damage.X.X5 import X5
from division2calc.build.damage.X.X6 import X6
from division2calc.build.damage.X.X7 import X7
from division2calc.build.damage.X.X8 import X8
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
        self.x3 = X3()
        self.x4 = X4()
        self.x5 = X5()
        self.x6 = X6(self._stats)
        self.x7 = X7(self._stats)
        self.x8 = X8(self._stats)

    def __getitem__(self, i: int) -> Profile[float]:
        if 1 <= i <= 8:
            return getattr(self, f'x{i}')
        else:
            raise IndexError(f'x{i}')
    #
    # use cases
    #

    @property
    def basic(self) -> X_Value:
        return {'x1': self[1].basic,
                'x2': self[2].basic,
                'x3': self[3].basic,
                'x4': self[4].basic,
                'x5': self[5].basic,
                'x5': self[6].basic,
                'x7': self[7].basic,
                'x8': self[8].basic}

    @property
    def min(self) -> X_Value:
        return {'x1': self[1].min,
                'x2': self[2].min,
                'x3': self[3].min,
                'x4': self[4].min,
                'x5': self[5].min,
                'x6': self[6].min,
                'x7': self[7].min,
                'x8': self[8].min}

    @property
    def average(self) -> X_Value:
        return {'x1': self[1].average,
                'x2': self[2].average,
                'x3': self[3].average,
                'x4': self[4].average,
                'x5': self[5].average,
                'x6': self[6].average,
                'x7': self[7].average,
                'x8': self[8].average}

    @property
    def max(self) -> X_Value:
        return {'x1': self[1].max,
                'x2': self[2].max,
                'x3': self[3].max,
                'x4': self[4].max,
                'x5': self[5].max,
                'x6': self[6].max,
                'x7': self[7].max,
                'x8': self[8].max}
