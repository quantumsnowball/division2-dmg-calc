from dataclasses import dataclass


@dataclass
class Watch:
    weapon_damage_score: int = 50

    @property
    def weapon_damage_pct(self) -> float:
        return self.weapon_damage_score * 0.002
