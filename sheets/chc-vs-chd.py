from dataclasses import replace

from division2calc import *

base = Build(
    name='base',
    # specialization
    specialization=Gunner(),
    # weapons
    weapon=AR.StElmosEngine(expertise_level=15),
    # gears
    mask=Striker.Mask(attr1=gearattrs.CHC(0.06),
                      mod=gearmods.CHD(0.12)),
    backpack=Striker.Backpack(mod=gearmods.CHD(0.12)),
    chest=Lengmo.Chest(mod=gearmods.CHD(0.119)),
    gloves=Striker.Gloves(),
    holster=Striker.Holster(),
    kneepads=Overlord.FoxsPrayer(attr2=gearattrs.CHC(0.06)),
)

builds = [base, ]
builds.append(replace(
    builds[-1],
    name='+1CHC',
    mask=Striker.Mask(attr1=gearattrs.CHC(0.06),
                      mod=gearmods.CHC(0.06)),
))
builds.append(replace(
    builds[-1],
    name='+2CHC',
    backpack=Striker.Backpack(mod=gearmods.CHC(0.06)),
))
builds.append(replace(
    builds[-1],
    name='+3CHC',
    chest=Lengmo.Chest(mod=gearmods.CHC(0.06)),
))
