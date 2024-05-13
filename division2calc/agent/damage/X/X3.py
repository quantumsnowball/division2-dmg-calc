from dataclasses import dataclass

import division2calc.agent.weapon.talents as talents
from division2calc.agent.damage.common import Profile
from division2calc.agent.weapon import Weapon


@dataclass
class X3(Profile[float]):
    _weapon: Weapon
    ''' 
    weapon talent amplifier
    '''
    @property
    def basic(self) -> float:
        return 1.0

    @property
    def min(self) -> float:
        return self.basic

    @property
    def average(self) -> float:
        x = 1.0
        # weapon
        if isinstance(self._weapon.talent, talents.Ranger):
            x += self._weapon.talent.avg_buff
        # result
        return x

    @property
    def max(self) -> float:
        x = 1.0
        # weapon
        if isinstance(self._weapon.talent, talents.Ranger):
            x += self._weapon.talent.max_buff
        # result
        return x
