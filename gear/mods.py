from dataclasses import dataclass


class Mod:
    pass


@dataclass
class CriticalHitChance(Mod):
    pct: float


@dataclass
class CriticalHitDamage(Mod):
    pct: float


@dataclass
class NoMod(Mod):
    pass
