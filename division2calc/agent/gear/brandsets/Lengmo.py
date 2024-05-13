from dataclasses import dataclass, field

import division2calc.agent.gear as gear
import division2calc.agent.gear.attrs as attrs
import division2calc.agent.gear.brandsets.bonus as bonus
import division2calc.agent.gear.talents as talents
from division2calc.agent.gear.brandsets import BonusPool, Brandsets


@dataclass(kw_only=True)
class Lengmo(Brandsets):
    brandset: str = 'Lengmo'
    bonus_pool: BonusPool = field(default=(bonus.ExploosiveResistance(0.2),
                                           bonus.SkillHealth(0.25),
                                           bonus.LMGDamage(0.3)), repr=False)


@dataclass(kw_only=True)
class Mask(gear.Mask, Lengmo):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.BlueCore(170_000))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.ExplosiveResistence(.10))
    attr2: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitChance(.06))


@dataclass(kw_only=True)
class Chest(gear.Chest, Lengmo):
    core: attrs.CoreAttribute = field(default_factory=lambda: attrs.BlueCore(170_000))
    attr1: attrs.MinorAttribute = field(default_factory=lambda: attrs.ExplosiveResistence(.10))
    attr2: attrs.MinorAttribute = field(default_factory=lambda: attrs.CriticalHitChance(.06))
    talent: talents.ChestTalent = field(default_factory=lambda: talents.Obliterate())
