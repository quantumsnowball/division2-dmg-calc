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
    critical_hit_chance: float
    critical_hit_damage: float
    headshot_damage: float
    damage_to_armor: float
    damage_to_health: float
    damage_to_target_out_of_cover: float

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

    #
    # multipliers
    #
    def x1(self) -> float:
        return 1+self.weapon_damage_pct+self.weapon_type_dmg_pct

    def x6(self, critical: bool = False, headshot: bool = False) -> float:
        x = 1
        if critical:
            x += self.critical_hit_damage
        if headshot:
            x += self.headshot_damage
        return x

    def x7(self, dtoArmor: bool = False, dtoHealth: bool = False) -> float:
        x = 1
        if dtoArmor:
            x += self.damage_to_armor
        if dtoHealth:
            x += self.damage_to_health
        return x

    def x8(self, dtooC: bool = False) -> float:
        x = 1
        if dtooC:
            x += self.damage_to_target_out_of_cover
        return x

    def total_damage(self,
                     *,
                     critical=False,
                     headshot=False,
                     dtoArmor=False,
                     dtoHealth=False,
                     dtooC=False) -> float:
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
            self.base_damage
            * self.x1()
            * self.x6(critical, headshot)
            * self.x7(dtoArmor, dtoHealth)
            * self.x8(dtooC)
        )

        # result
        return dmg

    def summary(self) -> str:
        s = '\n'.join((
            f'x1 (1 + wDmg    + wTypeDmg + wDmgTalent) : {self.x1():.2f}',
            f'x6 (1 + CritDmg + HSDmg)                 : {self.x6():.2f}',
            f'x7 (1 + DtA     + DtH)                   : {self.x7():.2f}',
            f'x8 (1 + DtooC)                           : {self.x8():.2f}',
        ))
        return s
