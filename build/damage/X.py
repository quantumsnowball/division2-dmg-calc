from dataclasses import dataclass
from typing import Literal

from build.stats import Stats
from gear import Gears
from weapon import Weapon
import gear.talents as talents
import gear.gearsets as gearsets
import gear.gearsets.bonus as gearsets_bonus


Name = Literal['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']
X_Value = dict[Name, float]


@dataclass
class X:
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

    @property
    def x1(self) -> float:
        return 1+self._stats.weapon_damage+self._stats.weapon_type_damage

    @property
    def x2(self) -> float:
        x = 1.0
        # backpack
        # chest
        if isinstance(self._gears.chest.talent, talents.Obliterate):
            x += self._gears.chest.talent.max
        # gearset
        for gear in self._gears:
            if isinstance(gear, gearsets.Gearsets):
                if isinstance(gear.gearset_bonus, gearsets_bonus.StrikersGamble):
                    x += gear.gearset_bonus.max
        # result
        return x

    @property
    def x2_min(self) -> float:
        return 1.0

    @property
    def x2_mean(self) -> float:
        x = 1.0
        # backpack
        # chest
        if isinstance(self._gears.chest.talent, talents.Obliterate):
            x += self._gears.chest.talent.average
        # gearset
        for gear in self._gears:
            if isinstance(gear, gearsets.Gearsets):
                if isinstance(gear.gearset_bonus, gearsets_bonus.StrikersGamble):
                    x += gear.gearset_bonus.average
        # result
        return x

    @property
    def x2_max(self) -> float:
        return self.x2

    def x6(self, critical: bool, headshot: bool) -> float:
        x = 1
        if critical:
            x += self._stats.critical_hit_damage
        if headshot:
            x += self._stats.headshot_damage
        # result
        return x

    @property
    def x6_min(self) -> float:
        return 1.0

    @property
    def x6_mean(self) -> float:
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
    def x7_mean(self) -> float:
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

    @property
    def x8(self) -> float:
        x = 1.0
        x += self._stats.damage_to_target_out_of_cover
        # result
        return x

    @property
    def basic(self) -> X_Value:
        return {'x1': self.x1,
                'x2': 1.0,
                'x6': 1.0,
                'x7': 1.0,
                'x8': self.x8}

    @property
    def min(self) -> X_Value:
        return {'x1': self.x1,
                'x2': self.x2_min,
                'x6': self.x6_min,
                'x7': self.x7_min,
                'x8': self.x8}

    @property
    def average(self) -> X_Value:
        return {'x1': self.x1,
                'x2': self.x2_mean,
                'x6': self.x6_mean,
                'x7': self.x7_mean,
                'x8': self.x8}

    @property
    def max(self) -> X_Value:
        return {'x1': self.x1,
                'x2': self.x2_max,
                'x6': self.x6_max,
                'x7': self.x7_max,
                'x8': self.x8}
