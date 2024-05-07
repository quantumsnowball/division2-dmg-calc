from dataclasses import dataclass

from gear.attribute import (CoreAttribute, CriticalHitDamage, MinorAttribute,
                            RedCore)


@dataclass(kw_only=True)
class Gear:
    name: str
    core: CoreAttribute
    attr1: MinorAttribute

    @property
    def weapon_damage_pct(self) -> float:
        if isinstance(self.core, RedCore):
            return self.core.weapon_damage_pct
        return 0.0

    @property
    def critical_hit_damage_pct(self) -> float:
        if isinstance(self.attr1, CriticalHitDamage):
            return self.attr1.pct
        return 0.0
