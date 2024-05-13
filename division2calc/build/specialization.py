from dataclasses import dataclass, field

from division2calc.utils import Float
from division2calc.weapon import WeaponType


@dataclass
class WeaponTypeBonus:
    AR: int = 3
    SMG: int = 3
    LMG: int = 3
    Rifle: int = 0
    MMR: int = 0
    Shotgun: int = 0


@dataclass(kw_only=True)
class Specialization:
    name: str
    weapon_type_damage_scores: WeaponTypeBonus = field(default_factory=WeaponTypeBonus)

    def weapon_type_damage(self, type: WeaponType) -> Float:
        unit = 0.05
        pct = getattr(self.weapon_type_damage_scores, type) * unit
        src = [f'{self.name}.{type}({pct:.2f})', ]
        return Float(pct, src)


@dataclass(kw_only=True)
class Gunner(Specialization):
    name: str = 'Gunner'
