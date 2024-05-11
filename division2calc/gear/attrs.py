from dataclasses import dataclass

#
# Core Attributes
#


@dataclass
class CoreAttribute:
    pass


@dataclass
class RedCore(CoreAttribute):
    damage: float = 0.15


@dataclass
class BlueCore(CoreAttribute):
    armor: int = 170_000


@dataclass
class SkillCore(CoreAttribute):
    tier: int = 1


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
    pct: float = 0.12


@dataclass
class HeadshotDamage(OffensiveMinorAttribute):
    pct: float = 0.10


CHC = CriticalHitChance
CHD = CriticalHitDamage
HS = HeadshotDamage


@dataclass
class DamageToHealth(OffensiveMinorAttribute):
    pct: float = 0.10


@dataclass
class DamageToTargetOutOfCover(OffensiveMinorAttribute):
    pct: float = 0.08


# defensive
@dataclass
class DefensiveMinorAttribute(MinorAttribute):
    pass


@dataclass
class ExplosiveResistence(DefensiveMinorAttribute):
    pct: float = 0.10


#
# Empty
#
@dataclass
class NoAttr(MinorAttribute):
    def __repr__(self) -> str:
        return 'N/A'
