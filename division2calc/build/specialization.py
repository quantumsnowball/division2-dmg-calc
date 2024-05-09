from dataclasses import dataclass, field

from division2calc.weapon import WeaponType


@dataclass(kw_only=True)
class Specialization:
    name: str
    weapon_type_damage_scores: dict[WeaponType, int] = field(
        default_factory=lambda: {
            'AR': 3, 'SMG': 3, 'LMG': 3,
            'Rifle': 0, 'MMR': 0, 'Shotgun': 0,
        })

    def weapon_type_damage(self, type: WeaponType) -> float:
        return self.weapon_type_damage_scores.get(type, 0) * 0.05


@dataclass(kw_only=True)
class Gunner(Specialization):
    name: str = 'Gunner'
