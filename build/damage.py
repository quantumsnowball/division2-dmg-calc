from dataclasses import dataclass

from build.stats import Stats
from gear import Gears
from weapon import Weapon


@dataclass
class _Multiplier:
    _weapon: Weapon
    _gears: Gears
    _stats: Stats

    #
    # factors
    #
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

    @property
    def x1(self) -> float:
        return 1+self._stats.weapon_damage+self._stats.weapon_type_damage

    def x6(self, critical: bool, headshot: bool) -> float:
        x = 1
        if critical:
            x += self._stats.critical_hit_damage
        if headshot:
            x += self._stats.headshot_damage
        # result
        return x

    @property
    def x6_mean(self) -> float:
        x = 1
        # weight by critical hit chance
        x += self._stats.critical_hit_chance*self._stats.critical_hit_damage
        # result
        return x

    def x7(self, armor: bool) -> float:
        x = 1
        if armor:
            x += self._stats.damage_to_armor
        else:
            x += self._stats.damage_to_health
        # result
        return x

    @property
    def x7_mean(self) -> float:
        # assuming equal chance for armor and health damage
        x = 1
        x += 0.5*self._stats.damage_to_armor + 0.5*self._stats.damage_to_health
        # result
        return x

    @property
    def x8(self) -> float:
        x = 1
        x += self._stats.damage_to_target_out_of_cover
        # result
        return x


@dataclass
class Damage:
    _weapon: Weapon
    _gears: Gears
    _stats: Stats

    def __post_init__(self) -> None:
        self._x = _Multiplier(self._weapon, self._gears, self._stats)

    @property
    def basic(self) -> float:
        # base
        dmg = self._weapon.base_damage
        # basic weapon damage
        dmg *= self._x.x1
        # result
        return dmg

    @property
    def average(self) -> float:
        # x6: weight by critical hit chance
        dmg = self.basic
        dmg *= self._x.x6_mean
        dmg *= self._x.x7_mean
        dmg *= self._x.x8
        # result
        return dmg

    def total_damage(self,
                     *,
                     critical: bool = False,
                     headshot: bool = False,
                     armor: bool = False):
        # base
        dmg = self._weapon.base_damage
        dmg *= self._x.x1
        dmg *= self._x.x6(critical, headshot)
        dmg *= self._x.x7(armor)
        dmg *= self._x.x8
        # result
        return dmg
