from dataclasses import dataclass


@dataclass
class Weapon:
    name: str
    base_damage: int
    expertise_level: int
    weapon_type_damage_bonus: float

    @property
    def weapon_damage_pct(self) -> float:
        return self.expertise_level * 0.01

    @property
    def weapon_type_damage_pct(self) -> float:
        return self.weapon_type_damage_bonus
