from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    base_damage: int
    expertise_level: int

    @property
    def weapon_damage_pct(self) -> float:
        return self.expertise_level * 0.01
