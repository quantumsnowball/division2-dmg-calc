from division2calc import *

base = Build(
    name='Striker Obliterate',
    # specialization
    specialization=Gunner(),
    # weapons
    weapon=AR.StElmosEngine(expertise_level=15),
    # gears
    mask=Striker.Mask(attr1=gearattrs.CHC(.06),
                      mod=gearmods.CHD(.12)),
    backpack=Striker.Backpack(mod=gearmods.CHC(.06)),
    chest=Lengmo.Chest(mod=gearmods.CHC(.06)),
    gloves=Striker.Gloves(),
    holster=Striker.Holster(),
    kneepads=Overlord.FoxsPrayer(attr2=gearattrs.CHC(.06)),
)

builds = [
    base,
    base.replace(
        name='Striker with Chest',
        mask=Lengmo.Mask(mod=gearmods.CHD(.12)),
        chest=Striker.Chest(mod=gearmods.CHC(.06)),
    ),
]
