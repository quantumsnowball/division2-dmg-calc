from dataclasses import dataclass, field

import gear.attribute as attrs
import gear.mods as mods


@dataclass(kw_only=True)
class Gear:
    name: str
    core: attrs.CoreAttribute
    attr1: attrs.MinorAttribute
    mod: mods.Mod = field(default_factory=mods.NoMod)

    @property
    def weapon_damage_pct(self) -> float:
        if isinstance(self.core, attrs.RedCore):
            return self.core.weapon_damage_pct
        return 0.0

    @property
    def critical_hit_chance_pct(self) -> float:
        pct = 0
        # attribute
        if isinstance(self.attr1, attrs.CriticalHitChance):
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
        if isinstance(self.attr1, attrs.CriticalHitDamage):
            pct += self.attr1.pct
        # mods
        if isinstance(self.mod, mods.CriticalHitDamage):
            pct += self.mod.pct

        # result
        return pct

    @property
    def headshot_damage_pct(self) -> float:
        pct = 0
        # attribute
        if isinstance(self.attr1, attrs.HeadshotDamage):
            pct += self.attr1.pct
        # mods
        if isinstance(self.mod, mods.HeadshotDamage):
            pct += self.mod.pct

        # result
        return pct

    @property
    def damage_to_health_pct(self) -> float:
        pct = 0
        # attribute
        if isinstance(self.attr1, attrs.DamageToHealth):
            pct += self.attr1.pct

        # result
        return pct
