from dataclasses import dataclass

from gear.attribute import CoreAttribute, RedCore


@dataclass(kw_only=True)
class Gear:
    name: str
    core: CoreAttribute

    @property
    def weapon_damage_pct(self) -> float:
        if isinstance(self.core, RedCore):
            return self.core.weapon_damage_pct
        return 0.0
