from build import Build

legendary1 = Build(
    name='Legendary1',
    base_damage=44191,
    n_red_core=5,
    watch_score=50,
    weapon_damage_bonus_pct=0.15,
    specialization_bonus_pct=0.15,
    expertise_level=17,
)


def main():
    print(legendary1)
    print(f'{legendary1.total_damage=:,.2f}')


if __name__ == '__main__':
    main()
