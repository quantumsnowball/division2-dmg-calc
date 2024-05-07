from build import Build
from gear import Gear
from weapon import Weapon


def main():
    Legendary1 = Build(
        name='Legendary1',
        weapon=Weapon("St Elmo's Engine", base_damage=44191),
        mask=Gear(name='Lengmo'),
        backpack=Gear(name='Striker'),
        chest=Gear(name='Striker'),
        gloves=Gear(name='Striker'),
        holster=Gear(name='Striker'),
        kneepads=Gear(name='Fox'),
    )

    print(Legendary1.summary())


if __name__ == '__main__':
    main()
