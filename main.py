from pprint import pprint

from tabulate import tabulate

import gear.attrs as gearattrs
import gear.Lengmo as lengmo
import gear.mods as gearmods
import gear.OverlordArmaments as overlord
import gear.Striker as striker
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
    print(tabulate(build.dmg_stats(), headers='keys', tablefmt='fancy_grid'))
    print(build.dmg_matrix().astype(int))


if __name__ == '__main__':
    main()
