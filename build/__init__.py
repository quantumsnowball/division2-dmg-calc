from dataclasses import dataclass, field

from build.specialization import Specialization
from build.watch import Watch
from gear import Gear
from weapon import Weapon

import pandas as pd


@dataclass
class Build:
    name: str
    weapon: Weapon
    mask: Gear
    backpack: Gear
    chest: Gear
    gloves: Gear
    holster: Gear
    kneepads: Gear
    specialization: Specialization
    watch: Watch = field(default_factory=Watch)

    def __post_init__(self) -> None:
        self.gears = (
            self.mask, self.backpack,
            self.chest, self.gloves,
            self.holster, self.kneepads
        )

    @property
    def weapon_damage_pct(self) -> float:
        pct = 0
        # gear core attributes
        for gear in self.gears:
            pct += gear.weapon_damage_pct
        # keener's watch
        pct += self.watch.weapon_damage_pct
        # expertise level
        pct += self.weapon.weapon_damage_pct

        # result
        return pct

    @property
    def weapon_type_dmg_pct(self) -> float:
        pct = 0
        # weapon attributes
        pct += self.weapon.weapon_type_damage_pct
        # specialization bonus
        pct += self.specialization.weapon_type_damage_pct(self.weapon.type)

        # result
        return pct

    @property
    def critical_hit_chance_pct(self) -> float:
        # base CHC
        pct = 0.0
        # weapon
        pct += self.weapon.critical_hit_chance_pct
        # gear
        for gear in self.gears:
            pct += gear.critical_hit_chance_pct
        # keener's watch
        pct += self.watch.critical_hit_chance_pct

        # result
        return pct

    @property
    def critical_hit_damage_pct(self) -> float:
        # base CHD
        pct = 0.25
        # weapon
        pct += self.weapon.critical_hit_damage_pct
        # gear
        for gear in self.gears:
            pct += gear.critical_hit_damage_pct
        # keener's watch
        pct += self.watch.critical_hit_damage_pct

        # result
        return pct

    @property
    def headshot_damage_pct(self) -> float:
        # base HS
        pct = 0.55
        # weapon
        pct += self.weapon.headshot_damage_pct
        # gear
        for gear in self.gears:
            pct += gear.headshot_damage_pct
        # keener's watch
        pct += self.watch.headshot_damage_pct

        # result
        return pct

    def x1(self) -> float:
        return 1+self.weapon_damage_pct+self.weapon_type_dmg_pct

    def x6(self, critical: bool, headshot: bool) -> float:
        x = 1
        if critical:
            x += self.critical_hit_damage_pct
        if headshot:
            x += self.headshot_damage_pct

        # result
        return x

    def total_damage(self,
                     *,
                     critical: bool,
                     headshot: bool):
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
        dmg = (
            self.weapon.base_damage
            * self.x1()
            * self.x6(critical, headshot)
        )

        # result
        return dmg

    def summary(self) -> pd.DataFrame:
        # columns
        x6_columns = {'Normal': (0, 0), 'Critical': (1, 0), 'Headshot': (0, 1), 'CriticalHeadshot': (1, 1)}
        x7_columns = {'Health': 0, 'Armor': 1}
        columns = pd.MultiIndex.from_product([x7_columns.keys(), x6_columns.keys()])
        # index
        index = pd.MultiIndex.from_product([['Basic'], ['Base']])
        # data
        data = [[self.total_damage(critical=crit, headshot=hs)
                 for arm in x7_columns.values()
                 for crit, hs in x6_columns.values()]]
        df = pd.DataFrame(data, index=index, columns=columns)

        # result
        return df
