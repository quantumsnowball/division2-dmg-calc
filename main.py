from pprint import pprint

from build import Build
from build.specialization import Gunner
from gear.attribute import CriticalHitChance
from gear.FoxPrayer import FoxPrayer
from gear.Lengmo import Lengmo
from gear.mods import CriticalHitDamage
from gear.Striker import Striker
from weapon.StElmosEngine import StElmosEngine


def main():
    build = Build(
        name='Legendary1',
        # specialization
        specialization=Gunner(),
        # weapons
        weapon=StElmosEngine(expertise_level=17),
        # gears
        mask=Striker(attr1=CriticalHitChance(0.06),
                     mod=CriticalHitDamage(0.12)),
        backpack=Striker(mod=CriticalHitDamage(0.12)),
        chest=Lengmo(mod=CriticalHitDamage(0.119)),
        gloves=Striker(),
        holster=Striker(),
        kneepads=FoxPrayer(attr1=CriticalHitChance(0.06)),
    )

    pprint(build)
    print(build.summary())
    print(f'{build.critical_hit_chance_pct=:.4f}')
    print(f'{build.critical_hit_damage_pct=:.4f}')
    print(f'{build.headshot_damage_pct=:.4f}')


if __name__ == '__main__':
    main()
