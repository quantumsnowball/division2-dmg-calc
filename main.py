from pprint import pprint

from tabulate import tabulate

import gear.attrs as gearattrs
import gear.mods as gearmods
from build import Build
from build.specialization import Gunner
from gear.FoxPrayer import FoxPrayer
from gear.Lengmo import Lengmo
from gear.Striker import Striker
from weapon.StElmosEngine import StElmosEngine


def main():
    build = Build(
        name='Legendary1',
        # specialization
        specialization=Gunner(),
        # weapons
        weapon=StElmosEngine(expertise_level=15),
        # gears
        mask=Striker(attr1=gearattrs.CHC(0.06),
                     mod=gearmods.CHD(0.12)),
        backpack=Striker(mod=gearmods.CHD(0.12)),
        chest=Lengmo(mod=gearmods.CHD(0.119)),
        gloves=Striker(),
        holster=Striker(),
        kneepads=FoxPrayer(attr2=gearattrs.CHC(0.06)),
    )

    pprint(build)
    print(tabulate(build.dmg_stats(), headers='keys', tablefmt='fancy_grid'))
    print(build.dmg_matrix().astype(int))


if __name__ == '__main__':
    main()
