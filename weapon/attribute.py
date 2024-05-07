from dataclasses import dataclass


class Attribute:
    pass


class CoreAttribute(Attribute):
    pass


class MinorAttribute(Attribute):
    pass


@dataclass
class AssultRifleDamage(CoreAttribute):
    weapon_type_damage_pct: float = 0.15


@dataclass
class HealthDamage(CoreAttribute):
    health_damage_pct: float = 0.21


@dataclass
class RateOfFire(MinorAttribute):
    rate_of_fire_pct: float = 0.05
