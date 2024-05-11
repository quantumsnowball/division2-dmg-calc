from dataclasses import dataclass


#
# Core Attribute
#
@dataclass
class CoreAttribute:
    pass


@dataclass
class AssultRifleDamage(CoreAttribute):
    pct: float = 0.15


@dataclass
class HealthDamage(CoreAttribute):
    pct: float = 0.21


#
# Minor Attribute
#
@dataclass
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
@dataclass
class NoAttr(MinorAttribute):
    def __repr__(self) -> str:
        return 'N/A'
