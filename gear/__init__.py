from dataclasses import dataclass


@dataclass
class Gear:
    name: str
    weapon_damage_bonus: float = 0.15
