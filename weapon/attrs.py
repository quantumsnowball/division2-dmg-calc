from dataclasses import dataclass


#
# Core Attribute
#
class CoreAttribute:
    pass


@dataclass
class AssultRifleDamage(CoreAttribute):
    weapon_type_damage_pct: float = 0.15


@dataclass
class HealthDamage(CoreAttribute):
    pct: float = 0.21


#
# Minor Attribute
#
class MinorAttribute:
    pass


@dataclass
class DamageToTargetOutOfCover(MinorAttribute):
    pct: float = 0.10


@dataclass
class RateOfFire(MinorAttribute):
    pct: float = 0.05


#
# Empty
#
class NoAttr(MinorAttribute):
    def __repr__(self) -> str:
        return 'N/A'
