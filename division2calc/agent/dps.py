from dataclasses import dataclass

import division2calc.agent.damage.common as common
import division2calc.agent.weapon.talents as weapon_talents
from division2calc.agent.damage import Damage
from division2calc.agent.stats import Stats
from division2calc.agent.weapon import Weapon


@dataclass
class DPS(common.Profile[float]):
    _weapon: Weapon
    _stats: Stats
    _damage: Damage

    @property
    def basic(self) -> float:
        rpm = self._weapon.rpm
        rof = self._stats.rate_of_fire
        dmg = self._damage.min
        # dps
        dps = rpm/60 * (1+rof) * dmg
        # result
        return dps

    @property
    def min(self) -> float:
        rpm = self._weapon.rpm
        rof = self._stats.rate_of_fire
        dmg = self._damage.min
        # special cases
        if isinstance(self._weapon.talent, weapon_talents.Measured):
            dmg = self._weapon.talent.adjust_dmg_min(dmg, self._damage.x[1].min, self._damage.x[2].min)
            rof += -self._weapon.talent.bottom_rof_dec
        # dps
        dps = rpm/60 * (1+rof) * dmg
        # result
        return dps

    @property
    def average(self) -> float:
        rpm = self._weapon.rpm
        rof = self._stats.rate_of_fire
        dmg = self._damage.average
        # special cases
        if isinstance(self._weapon.talent, weapon_talents.Measured):
            rof += self._weapon.talent.average_rof
        # dps
        dps = rpm/60 * (1+rof) * dmg
        # result
        return dps

    @property
    def max(self) -> float:
        rpm = self._weapon.rpm
        rof = self._stats.rate_of_fire
        dmg = self._damage.max
        # special cases
        if isinstance(self._weapon.talent, weapon_talents.Measured):
            dmg = self._weapon.talent.adjust_dmg_max(dmg, self._damage.x[1].max, self._damage.x[2].max)
            rof += +self._weapon.talent.top_rof_inc
        # dps
        dps = rpm/60 * (1+rof) * dmg
        # result
        return dps
