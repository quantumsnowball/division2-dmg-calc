from dataclasses import dataclass


class Mod:
    pass


@dataclass
class CriticalHitChance(Mod):
    pct: float


CHC = CriticalHitChance


@dataclass
class CriticalHitDamage(Mod):
    pct: float


CHD = CriticalHitDamage


@dataclass
class HeadshotDamage(Mod):
    pct: float


HS = HeadshotDamage


# Empty
class NoMod(Mod):
    def __repr__(self) -> str:
        return 'N/A'
