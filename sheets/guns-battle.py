from dataclasses import replace

from division2calc import *

base = Build(
    name='StElmosEngine',
    # specialization
    specialization=Gunner(),
    # weapons
    weapon=AR.StElmosEngine(expertise_level=15),
    # gears
    mask=Striker.Mask(attr1=gearattrs.CHC(.06),
                      mod=gearmods.CHD(.12)),
    backpack=Striker.Backpack(mod=gearmods.CHD(.12)),
    chest=Lengmo.Chest(mod=gearmods.CHC(.06)),
    gloves=Striker.Gloves(),
    holster=Striker.Holster(),
    kneepads=Overlord.FoxsPrayer(attr2=gearattrs.CHC(.06)),
)

builds = [base, ]
builds.append(replace(
    builds[-1],
    name='ShieldSplinterer',
    weapon=AR.ShieldSplinterer(expertise_level=12),
))
builds.append(replace(
    builds[-1],
    name='BulletKing',
    weapon=LMG.BulletKing(expertise_level=18),
))
