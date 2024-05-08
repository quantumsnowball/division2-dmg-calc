from dataclasses import dataclass, field

from build.stats import Stats
import gear
from build.specialization import Specialization
from build.watch import Watch
import gear.utils as utils
from weapon import Weapon

import pandas as pd


@dataclass
class Build:
    name: str
    weapon: Weapon
    mask: gear.Mask
    backpack: gear.Backpack
    chest: gear.Chest
    gloves: gear.Gloves
    holster: gear.Holster
    kneepads: gear.Kneepads
    specialization: Specialization
    watch: Watch = field(default_factory=Watch)

    def __post_init__(self) -> None:
        self.gears = (
            self.mask, self.backpack,
            self.chest, self.gloves,
            self.holster, self.kneepads
        )
        self.stats = Stats(self.weapon, self.gears, self.watch, self.specialization)
        # enable brandset bonus
        utils.enable_brandset_bonus(self.gears)
        # enable gearset bonus
        utils.enable_gearset_bonus(self.gears)

    #
    # factors
    #

    def x1(self) -> float:
        return 1+self.stats.weapon_damage_pct+self.stats.weapon_type_dmg_pct

    def x6(self, critical: bool, headshot: bool) -> float:
        x = 1
        if critical:
            x += self.stats.critical_hit_damage_pct
        if headshot:
            x += self.stats.headshot_damage_pct

        # result
        return x

    def x7(self, armor: bool) -> float:
        x = 1
        if armor:
            x += self.stats.damage_to_armor_pct
        else:
            x += self.stats.damage_to_health_pct

        # result
        return x

    def x8(self) -> float:
        x = 1
        x += self.stats.damage_to_target_out_of_cover_pct

        # result
        return x

    def total_damage(self,
                     *,
                     critical: bool = False,
                     headshot: bool = False,
                     armor: bool = False,
                     basic: bool = False):
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
        # base
        dmg = self.weapon.base_damage
        dmg *= self.x1()
        if basic:
            # result - basic weapon damage
            return dmg
        dmg *= self.x6(critical, headshot)
        dmg *= self.x7(armor)
        dmg *= self.x8()

        # result
        return dmg

    def dmg_stats(self) -> pd.DataFrame:
        # data
        data = {
            'WeaponDamage': f'{self.total_damage(basic=True):,.0f}',
            'CriticalHitChance': f'{self.stats.critical_hit_chance_pct:.1%}',
            'CriticalHitDamage': f'{self.stats.critical_hit_damage_pct:.1%}',
            'HeadshotDamage': f'{self.stats.headshot_damage_pct:.1%}',
            'ArmorDamage': f'{self.stats.damage_to_armor_pct:.1%}',
            'HealthDamage': f'{self.stats.damage_to_health_pct:.1%}',
        }
        df = pd.DataFrame(data, index=['%'])

        # result
        return df

    def dmg_matrix(self) -> pd.DataFrame:
        # columns
        x6_columns = {'Normal': (False, False), 'Critical': (True, False),
                      'Headshot': (False, True), 'CritHead': (True, True)}
        x7_columns = {'Health': False, 'Armor': True}
        columns = pd.MultiIndex.from_product([x7_columns.keys(), x6_columns.keys()])
        # index
        scenario_index = {'Basic': False}
        talent_index = {'Base': False}
        index = pd.MultiIndex.from_product([scenario_index.keys(), talent_index.keys()])
        # data
        data = [[self.total_damage(critical=crit, headshot=hs, armor=arm)
                 for arm in x7_columns.values()
                 for crit, hs in x6_columns.values()]
                for _ in scenario_index.values()
                for _ in talent_index.values()]
        df = pd.DataFrame(data, index=index, columns=columns)

        # result
        return df
