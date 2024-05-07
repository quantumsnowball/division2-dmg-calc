from dataclasses import dataclass


@dataclass
class Gear:
    name: str
    weapon_damage_pct: float = 0.15
