from dataclasses import dataclass


class Attribute:
    pass


class CoreAttribute(Attribute):
    pass


class MinorAttribute(Attribute):
    pass


@dataclass
class RedCore(CoreAttribute):
    weapon_damage_pct: float = 0.15


@dataclass
class BlueCore(CoreAttribute):
    armor: int = 170_000


@dataclass
class SkillCore(CoreAttribute):
    tier: int = 1


@dataclass
class CriticalHitChance(MinorAttribute):
    pct: float = 0.06


CHC = CriticalHitChance


@dataclass
class CriticalHitDamage(MinorAttribute):
    pct: float = 0.12


CHD = CriticalHitDamage


@dataclass
class HeadshotDamage(MinorAttribute):
    pct: float = 0.10


HS = HeadshotDamage
