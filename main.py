from pprint import pprint

from tabulate import tabulate

import gear.attrs as gearattrs
import gear.brandsets.Lengmo as lengmo
import gear.brandsets.OverlordArmaments as overlord
import gear.gearsets.StrikersBattlegear as striker
import gear.mods as gearmods
from build import Build
from build.specialization import Gunner
from weapon.StElmosEngine import StElmosEngine


def main():
    build = Build(
        name='Legendary1',
        # specialization
        specialization=Gunner(),
        # weapons
        weapon=StElmosEngine(expertise_level=15),
        # gears
        mask=striker.Mask(attr1=gearattrs.CHC(0.06),
                          mod=gearmods.CHD(0.12)),
        backpack=striker.Backpack(mod=gearmods.CHD(0.12)),
        chest=lengmo.Chest(mod=gearmods.CHD(0.119)),
        gloves=striker.Gloves(),
        holster=striker.Holster(),
        kneepads=overlord.FoxsPrayer(attr2=gearattrs.CHC(0.06)),
    )

    pprint(build)
    print(tabulate(build.summary.stats(), headers='keys', tablefmt='fancy_grid'))
    print(build.summary.damage().astype(int))
    print(f'{build.damage.basic=:.2f} {build.damage.average=:.2f} {build.damage.max=:.2f}')
    pprint(build.damage.x.basic)
    pprint(build.damage.x.average)
    pprint(build.damage.x.max)


if __name__ == '__main__':
    main()
