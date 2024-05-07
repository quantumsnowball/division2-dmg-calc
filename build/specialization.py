from dataclasses import dataclass


@dataclass
class Specialization:
    name: str
    weapon_type_damage_score: int = 3

    @property
    def weapon_type_damage_pct(self) -> float:
        return self.weapon_type_damage_score * 0.05
