from dataclasses import dataclass


@dataclass
class Watch:
    weapon_damage_score: int = 50
    critical_hit_chance_score: int = 50
    critical_hit_damage_score: int = 50
    headshot_damage_score: int = 50

    @property
    def weapon_damage(self) -> float:
        return self.weapon_damage_score * 0.002

    @property
    def critical_hit_chance(self) -> float:
        return self.critical_hit_chance_score * 0.002

    @property
    def critical_hit_damage(self) -> float:
        return self.critical_hit_damage_score * 0.004

    @property
    def headshot_damage(self) -> float:
        return self.headshot_damage_score * 0.004
