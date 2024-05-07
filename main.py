from build import Build
from build.specialization import Gunner
from gear import Gear
from gear.Striker import Striker
from weapon.StElmosEngine import StElmosEngine


def main():
    build = Build(
        name='Legendary1',
        specialization=Gunner(),
        weapon=StElmosEngine(expertise_level=17),
        mask=Gear(name='Lengmo', core='blue'),
        backpack=Striker(),
        chest=Striker(),
        gloves=Striker(),
        holster=Striker(),
        kneepads=Striker(),
    )

    print(build.summary())


if __name__ == '__main__':
    main()
