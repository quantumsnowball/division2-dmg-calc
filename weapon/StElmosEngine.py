from dataclasses import dataclass

from weapon import Weapon, WeaponType


@dataclass(kw_only=True)
class StElmosEngine(Weapon):
    expertise_level: int
    # presets
    name: str = "St Elmo's Engine"
    type: WeaponType = 'AR'
    base_damage: int = 44191
    weapon_type_damage_bonus: float = 0.15
