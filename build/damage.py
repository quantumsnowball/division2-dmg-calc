from dataclasses import dataclass

from build.stats import Stats
from gear import Gears
from weapon import Weapon


@dataclass
class Damage:
    weapon: Weapon
    gears: Gears
    stats: Stats

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
