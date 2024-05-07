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
        weapon=StElmosEngine(expertise_level=17),
        # gears
        mask=Lengmo(),
        backpack=Striker(),
        chest=Striker(),
        gloves=Striker(),
        holster=Striker(),
        kneepads=FoxPrayer(),
    )

    print(build.summary())
    print(f'{build.critical_hit_damage_pct=:.4f}')


if __name__ == '__main__':
    main()
