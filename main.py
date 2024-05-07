from build import Build, specialization
from build.specialization import Gunner, Specialization
from gear import Gear
from weapon import Weapon
from weapon.StElmosEngine import StElmosEngine


def main():
    build = Build(
        name='Legendary1',
        specialization=Gunner(),
        weapon=StElmosEngine(expertise_level=17),
        mask=Gear(name='Lengmo', core='blue'),
        backpack=Gear(name='Striker', core='red'),
        chest=Gear(name='Striker', core='red'),
        gloves=Gear(name='Striker', core='red'),
        holster=Gear(name='Striker', core='red'),
        kneepads=Gear(name='Fox', core='red'),
    )

    print(build.summary())


if __name__ == '__main__':
    main()
