from dataclasses import dataclass, field

import gear.attribute as attr
import gear.mods as mods


@dataclass(kw_only=True)
class Gear:
    name: str
    core: attr.CoreAttribute
    attr1: attr.MinorAttribute
    mod: mods.Mod = field(default_factory=mods.NoMod)

    @property
    def weapon_damage_pct(self) -> float:
        if isinstance(self.core, attr.RedCore):
            return self.core.weapon_damage_pct
        return 0.0

    @property
    def critical_hit_chance_pct(self) -> float:
        pct = 0
        # attribute
        if isinstance(self.attr1, attr.CriticalHitChance):
            pct += self.attr1.pct
        # mods
        if isinstance(self.mod, mods.CriticalHitChance):
            pct += self.mod.pct

        # result
        return pct

    @property
    def critical_hit_damage_pct(self) -> float:
        pct = 0
        # attribute
        if isinstance(self.attr1, attr.CriticalHitDamage):
            pct += self.attr1.pct
        # mods
        if isinstance(self.mod, mods.CriticalHitDamage):
            pct += self.mod.pct

        # result
        return pct
