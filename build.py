from dataclasses import dataclass


@dataclass
class Build:
    name: str
    base_damage: int
    n_red_core: int
    watch_score: int
    weapon_damage_bonus_pct: float
    specialization_bonus_pct: float
    expertise_level: int

    @property
    def weapon_damage_pct(self) -> float:
        # num of red core
        pct = self.n_red_core * 0.15
        # keener's watch
        pct += self.watch_score * 0.002
        # expertise level
        pct += self.expertise_level * 0.01

        # result
        return pct

    @property
    def weapon_type_dmg_pct(self) -> float:
        # weapon attributes
        pct = self.weapon_damage_bonus_pct
        # specialization bonus
        pct += self.specialization_bonus_pct

        # result
        return pct

    @property
    def total_damage(self) -> float:
        '''
        Total Damage = 
        Base weapon Damage 
            *(1+Weapon Damage+Weapon Type Damage+Weapon Damage Talents)
            *(1+Total Weapon Damage Talents) [Vigilance]
            *(1+Amplfied Talent 1)
            *(1+Amplfied Talent 2)
            *(1+Amplfied Talent 3)
            *(1+Critical Hit Damage+Headshot Damage)
            *(1+Damage to Armor+Damage to Health)
            *(1+Damage out of Cover)
        '''
        dmg = self.base_damage
        dmg *= 1+self.weapon_damage_pct+self.weapon_type_dmg_pct

        # result
        return dmg
