from build import Build
from weapon import Weapon


def main():
    Legendary1 = Build(
        name='Legendary1',
        weapon=Weapon("St Elmo's Engine", base_damage=44191)
    )

    print(Legendary1)


if __name__ == '__main__':
    main()
