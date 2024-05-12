from dataclasses import dataclass

from division2calc.build.specialization import Specialization
from division2calc.build.watch import Watch
from division2calc.gear import Gears
from division2calc.utils import Float
from division2calc.weapon import Weapon


@dataclass
class Stats:
    _weapon: Weapon
    _gears: Gears
    _watch: Watch
    _specialization: Specialization

    @property
    def weapon_damage(self) -> Float:
        pct = 0
        # gear core attributes
        for gear in self._gears:
            pct += gear.weapon_damage
        # keener's watch
        pct += self._watch.weapon_damage
        # expertise level
        pct += self._weapon.weapon_damage
        # result
        return Float(pct)

    @property
    def weapon_type_damage(self) -> Float:
        pct = 0
        # weapon attributes
        pct += self._weapon.weapon_type_damage
        # specialization bonus
        pct += self._specialization.weapon_type_damage(self._weapon.type)
        # result
        return Float(pct)

    @property
    def critical_hit_chance(self) -> Float:
        # base CHC
        pct = 0.0
        # weapon
        pct += self._weapon.critical_hit_chance
        # gear
        for gear in self._gears:
            pct += gear.critical_hit_chance
        # keener's watch
        pct += self._watch.critical_hit_chance
        # hard cap to 60%
        pct = min(0.6, pct)
        # result
        return Float(pct)

    @property
    def critical_hit_damage(self) -> Float:
        # base CHD
        pct = 0.25
        # weapon
        pct += self._weapon.critical_hit_damage
        # gear
        for gear in self._gears:
            pct += gear.critical_hit_damage
        # keener's watch
        pct += self._watch.critical_hit_damage
        # result
        return Float(pct)

    @property
    def headshot_damage(self) -> Float:
        # base HS
        pct = 0.55
        # weapon
        pct += self._weapon.headshot_damage
        # gear
        for gear in self._gears:
            pct += gear.headshot_damage
        # keener's watch
        pct += self._watch.headshot_damage
        # result
        return Float(pct)

    @property
    def damage_to_armor(self) -> Float:
        pct = 0
        # weapon
        # TODO
        # gear
        # TODO
        # result
        return Float(pct)

    @property
    def damage_to_health(self) -> Float:
        pct = 0
        # weapon
        pct += self._weapon.damage_to_health
        # gear
        for gear in self._gears:
            pct += gear.damage_to_health
        # result
        return Float(pct)

    @property
    def damage_to_target_out_of_cover(self) -> Float:
        pct = 0
        # weapon
        pct += self._weapon.damage_to_target_out_of_cover
        # gear
        for gear in self._gears:
            pct += gear.damage_to_target_out_of_cover
        # result
        return Float(pct)
