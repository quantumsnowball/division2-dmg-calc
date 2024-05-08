from dataclasses import dataclass

from build.damage import Damage
from build.stats import Stats

import pandas as pd


@dataclass
class Summary:
    _stats: Stats
    _damage: Damage

    def stats(self) -> pd.DataFrame:
        # data
        data = {
            'WeaponDamage': f'{self._damage.basic:,.0f}',
            'CriticalHitChance': f'{self._stats.critical_hit_chance:.1%}',
            'CriticalHitDamage': f'{self._stats.critical_hit_damage:.1%}',
            'HeadshotDamage': f'{self._stats.headshot_damage:.1%}',
            'ArmorDamage': f'{self._stats.damage_to_armor:.1%}',
            'HealthDamage': f'{self._stats.damage_to_health:.1%}',
        }
        df = pd.DataFrame(data, index=['%'])

        # result
        return df

    @property
    def x(self) -> pd.DataFrame:
        data = dict(basic=self._damage.x.basic,
                    min=self._damage.x.min,
                    average=self._damage.x.average,
                    max=self._damage.x.max)
        return pd.DataFrame(data).T

    @property
    def dydx(self) -> pd.DataFrame:
        data = dict(basic=self._damage.dydx.basic,
                    min=self._damage.dydx.min,
                    average=self._damage.dydx.average,
                    max=self._damage.dydx.max)
        return pd.DataFrame(data).T

    def damage(self) -> pd.DataFrame:
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
        data = [[self._damage.total_damage(critical=crit, headshot=hs, armor=arm)
                 for arm in x7_columns.values()
                 for crit, hs in x6_columns.values()]
                for _ in scenario_index.values()
                for _ in talent_index.values()]
        df = pd.DataFrame(data, index=index, columns=columns)

        # result
        return df
