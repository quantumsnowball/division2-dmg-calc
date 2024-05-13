from dataclasses import dataclass

from division2calc.utils import Float


@dataclass
class Watch:
    weapon_damage_score: int = 50
    critical_hit_chance_score: int = 50
    critical_hit_damage_score: int = 50
    headshot_damage_score: int = 50

    @property
    def weapon_damage(self) -> Float:
        unit = 0.002
        pct = self.weapon_damage_score * unit
        src = [f'{self.__class__.__name__}({pct})', ]
        return Float(pct, src)

    @property
    def critical_hit_chance(self) -> Float:
        return Float(self.critical_hit_chance_score * 0.002)

    @property
    def critical_hit_damage(self) -> Float:
        return Float(self.critical_hit_damage_score * 0.004)

    @property
    def headshot_damage(self) -> Float:
        return Float(self.headshot_damage_score * 0.004)
