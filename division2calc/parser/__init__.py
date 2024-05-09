from pathlib import Path

from division2calc.build import Build


def parse_build_yaml(yaml: Path) -> Build:
    print(yaml)
    print(type(yaml))
