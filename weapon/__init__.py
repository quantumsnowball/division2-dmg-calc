from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    base_damage: int
    expertise_level: int
