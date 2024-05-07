from dataclasses import dataclass

from gear.attribute import (CoreAttribute, CriticalHitDamage, MinorAttribute,
                            RedCore)


@dataclass(kw_only=True)
class Gear:
    name: str
    core: CoreAttribute
    minor: MinorAttribute

    @property
    def weapon_damage_pct(self) -> float:
        if isinstance(self.core, RedCore):
            return self.core.weapon_damage_pct
        return 0.0

    @property
    def critical_hit_damage_pct(self) -> float:
        if isinstance(self.minor, CriticalHitDamage):
            return self.minor.pct
        return 0.0
