from dataclasses import replace

from division2calc import *

base = Build(
    name='StElmosEngine',
    # specialization
    specialization=Gunner(),
    # weapons
    weapon=AR.StElmosEngine(expertise_level=18),
    # gears
    mask=Striker.Mask(attr1=gearattrs.CHC(.06),
                      mod=gearmods.CHD(.12)),
    backpack=Striker.Backpack(mod=gearmods.CHD(.12)),
    chest=Lengmo.Chest(mod=gearmods.CHC(.06)),
    gloves=Striker.Gloves(),
    holster=Striker.Holster(),
    kneepads=Overlord.FoxsPrayer(attr2=gearattrs.CHC(.06)),
)

builds = [
    base,
    base.replace(
        name='ShieldSplinterer',
        weapon=AR.ShieldSplinterer(expertise_level=12),
    ),
    base.replace(
        name='BulletKing',
        weapon=LMG.BulletKing(expertise_level=18),
    ),
    base.replace(
        name='GR9',
        weapon=LMG.GR9(expertise_level=0),
    ),
]
