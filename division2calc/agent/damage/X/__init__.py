from dataclasses import dataclass
from typing import Literal

from division2calc.agent.damage.common import Profile
from division2calc.agent.damage.X.X1 import X1
from division2calc.agent.damage.X.X2 import X2
from division2calc.agent.damage.X.X3 import X3
from division2calc.agent.damage.X.X4 import X4
from division2calc.agent.damage.X.X5 import X5
from division2calc.agent.damage.X.X6 import X6
from division2calc.agent.damage.X.X7 import X7
from division2calc.agent.damage.X.X8 import X8
from division2calc.agent.stats import Stats
from division2calc.gear import Gears
from division2calc.weapon import Weapon

Name = str
X_Value = dict[Name, float]


@dataclass
class X(Profile[X_Value]):
    _weapon: Weapon
    _gears: Gears
    _stats: Stats

    '''
    [Exact]
    DMG = Base weapon Damage
    x1|    *(1+Weapon Damage+Weapon Type Damage+Weapon Damage Talents)
    x2|    *(1+Total Weapon Damage Talents) [Vigilance]
    x3|    *(1+Amplfied Talent 1)
    x4|    *(1+Amplfied Talent 2)
    x5|    *(1+Amplfied Talent 3)
    x6|    *(1+Critical Hit Damage+Headshot Damage)
    x7|    *(1+Damage to Armor+Damage to Health)
    x8|    *(1+Damage out of Cover)

    [Expected] 
    DMG = Base weapon damage
    x1|    * (1 + WD + weapon type damage + sum of ("weapon damage" talents * talent uptime))
    x2|    * (1 + sum of ("total weapon damage" talents * talent uptime))
    x3|    * (1 + "amplify" talent1 * uptime)
    x4|    * (1 + "amplify" talent2 * uptime)
    x5|    * (1 + "amplify" talent3 * uptime)
    x6|    * (1 + CHC * CHD + HsD * headshot chance)
    x7|    * (1 + DtA * %Armor + DtH * (1 - %Armor))
    x8|    * (1 + OoCD * %OutOfCover)  
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
        return {
            f'x{i}': self[i].basic
            for i in range(1, 9)
        }

    @property
    def min(self) -> X_Value:
        return {
            f'x{i}': self[i].min
            for i in range(1, 9)
        }

    @property
    def average(self) -> X_Value:
        return {
            f'x{i}': self[i].average
            for i in range(1, 9)
        }

    @property
    def max(self) -> X_Value:
        return {
            f'x{i}': self[i].max
            for i in range(1, 9)
        }
