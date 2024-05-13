from dataclasses import dataclass

#
# Core Attributes
#


@dataclass
class CoreAttribute:
    pass


@dataclass
class RedCore(CoreAttribute):
    damage: float


@dataclass
class BlueCore(CoreAttribute):
    armor: int


@dataclass
class SkillCore(CoreAttribute):
    tier: int


#
# Minor Attributes
#

@dataclass
class MinorAttribute:
    pass


# offensive
@dataclass
class OffensiveMinorAttribute(MinorAttribute):
    pass


@dataclass
class CriticalHitChance(OffensiveMinorAttribute):
    pct: float = 0.06


@dataclass
class CriticalHitDamage(OffensiveMinorAttribute):
    pct: float


@dataclass
class HeadshotDamage(OffensiveMinorAttribute):
    pct: float


CHC = CriticalHitChance
CHD = CriticalHitDamage
HS = HeadshotDamage


@dataclass
class DamageToHealth(OffensiveMinorAttribute):
    pct: float


@dataclass
class DamageToTargetOutOfCover(OffensiveMinorAttribute):
    pct: float


# defensive
@dataclass
class DefensiveMinorAttribute(MinorAttribute):
    pass


@dataclass
class ExplosiveResistence(DefensiveMinorAttribute):
    pct: float


#
# Empty
#
@dataclass
class NoAttr(MinorAttribute):
    def __repr__(self) -> str:
        return 'N/A'
