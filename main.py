from build import Build, specialization
from build.specialization import Specialization
from gear import Gear
from weapon import Weapon


def main():
    build = Build(
        name='Legendary1',
        specialization=Specialization('Gunner'),
        weapon=Weapon("St Elmo's Engine", base_damage=44191, expertise_level=17, weapon_type_damage_bonus=0.15),
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
