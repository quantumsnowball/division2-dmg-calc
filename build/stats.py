from dataclasses import dataclass
from build.specialization import Specialization
from build.watch import Watch
from gear import Gears
from weapon import Weapon


@dataclass
class Stats:
    weapon: Weapon
    gears: Gears
    watch: Watch
    specialization: Specialization

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

    @property
    def damage_to_armor_pct(self) -> float:
        pct = 0
        # weapon
        # TODO
        # gear
        # TODO

        # result
        return pct

    @property
    def damage_to_health_pct(self) -> float:
        pct = 0
        # weapon
        pct += self.weapon.damage_to_health_pct
        # gear
        for gear in self.gears:
            pct += gear.damage_to_health_pct

        # result
        return pct

    @property
    def damage_to_target_out_of_cover_pct(self) -> float:
        pct = 0
        # weapon
        pct += self.weapon.damage_to_target_out_of_cover_pct
        # gear
        for gear in self.gears:
            pct += gear.damage_to_target_out_of_cover_pct

        # result
        return pct
