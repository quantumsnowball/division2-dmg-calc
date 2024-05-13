from dataclasses import dataclass


#
# Core Attribute
#
@dataclass
class CoreAttribute:
    pass


@dataclass
class AssultRifleDamage(CoreAttribute):
    pct: float


@dataclass
class LMGDamage(CoreAttribute):
    pct: float


@dataclass
class HealthDamage(CoreAttribute):
    pct: float


#
# Minor Attribute
#
@dataclass
class MinorAttribute:
    pass


@dataclass
class CriticalHitChance(MinorAttribute):
    pct: float


@dataclass
class CriticalHitDamage(MinorAttribute):
    pct: float


@dataclass
class DamageToTargetOutOfCover(CoreAttribute, MinorAttribute):
    pct: float


@dataclass
class RateOfFire(MinorAttribute):
    pct: float


#
# Empty
#
@dataclass
class NoAttr(MinorAttribute):
    def __repr__(self) -> str:
        return 'N/A'
