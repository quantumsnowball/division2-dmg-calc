from dataclasses import dataclass


@dataclass
class Mod:
    pass


@dataclass
class CriticalHitChance(Mod):
    pct: float


@dataclass
class CriticalHitDamage(Mod):
    pct: float


@dataclass
class HeadshotDamage(Mod):
    pct: float


CHC = CriticalHitChance
CHD = CriticalHitDamage
HS = HeadshotDamage


#
# Empty
#
@dataclass
class NoMod(Mod):
    def __repr__(self) -> str:
        return 'N/A'
