from dataclasses import dataclass, field

from build.specialization import Specialization
from build.watch import Watch
from gear import Gear
from weapon import Weapon


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
    def critical_hit_damage_pct(self) -> float:
        # base CHD
        pct = 0.25
        # weapon
        pct += self.weapon.critical_hit_damage_pct
        # gear
        for gear in self.gears:
            pct += gear.critical_hit_damage_pct

        # result
        return pct

    def x1(self) -> float:
        return 1+self.weapon_damage_pct+self.weapon_type_dmg_pct

    def total_damage(self):
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
        )

        # result
        return dmg

    def summary(self) -> str:
        return f'{self.total_damage()=:.2f}'
