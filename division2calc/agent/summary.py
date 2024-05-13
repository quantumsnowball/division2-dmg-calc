from dataclasses import dataclass

import pandas as pd

from division2calc.agent.common import PROFILES, Profiles
from division2calc.agent.damage import Damage
from division2calc.agent.stats import Stats


@dataclass
class Summary:
    _stats: Stats
    _damage: Damage

    @property
    def stats(self) -> pd.DataFrame:
        data = dict(basic={
            'WeaponDamage': self._damage.basic,
            'CriticalHitChance': self._stats.critical_hit_chance,
            'CriticalHitDamage': self._stats.critical_hit_damage,
            'HeadshotDamage': self._stats.headshot_damage,
            'ArmorDamage': self._stats.damage_to_armor,
            'HealthDamage': self._stats.damage_to_health,
        })
        df = pd.DataFrame.from_dict(data, orient='index')
        # result
        return df

    @property
    def x(self) -> pd.DataFrame:
        data = dict(basic=self._damage.x.basic,
                    min=self._damage.x.min,
                    average=self._damage.x.average,
                    max=self._damage.x.max)
        df = pd.DataFrame.from_dict(data, orient='index')
        df.index.names = ('profile',)
        df.columns.names = ('x',)
        return df

    @property
    def dydx(self) -> pd.DataFrame:
        data = dict(basic=self._damage.dydx.basic,
                    min=self._damage.dydx.min,
                    average=self._damage.dydx.average,
                    max=self._damage.dydx.max)
        df = pd.DataFrame.from_dict(data, orient='index')
        df.index.names = ('profile',)
        df.columns.names = ('dydx',)
        return df

    @property
    def damage(self) -> pd.DataFrame:
        # columns
        x6_columns = {'Normal': (False, False, False), 'Critical': (True, False, False),
                      'ExpCrit': (True, False, True),
                      'Headshot': (False, True, False), 'CritHead': (True, True, False)}
        x7_columns = {'Health': False, 'Armor': True}
        columns = pd.MultiIndex.from_product([x7_columns.keys(), x6_columns.keys()])
        columns.names = ('health/armor', 'critical/headshot')
        # index
        profile_index: Profiles = PROFILES
        index = pd.Index(profile_index, name='profile')
        # data
        data = [[self._damage.total_damage(profile, critical=crit, headshot=hs, expcrit=expcrit, armor=arm)
                 for arm in x7_columns.values()
                 for crit, hs, expcrit in x6_columns.values()]
                for profile in profile_index]
        df = pd.DataFrame(data, index=index, columns=columns)
        # result
        return df
