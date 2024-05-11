from pprint import pprint

from tabulate import tabulate

import division2calc.gear.attrs as gearattrs
import division2calc.gear.brandsets.Lengmo as lengmo
import division2calc.gear.brandsets.OverlordArmaments as overlord
import division2calc.gear.gearsets.StrikersBattlegear as striker
import division2calc.gear.mods as gearmods
from division2calc.build import Build
from division2calc.build.specialization import Gunner
from division2calc.weapon.StElmosEngine import StElmosEngine


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
    print(build.summary.damage.astype(int))
    print(f'{build.damage.basic=:.2f} {build.damage.average=:.2f} {build.damage.max=:.2f}')
    print('\nx:')
    print(build.summary.x.round(2))
    print('\ndydx:')
    print(build.summary.dydx.round(2))


if __name__ == '__main__':
    main()
