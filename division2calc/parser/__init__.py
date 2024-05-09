from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, field_validator

from division2calc.build.specialization import Gunner


class BuildData(BaseModel):
    name: str
    specialization: dict[str, Any]

    @field_validator('specialization')
    def ensure1(cls, v: dict[str, Any]) -> dict[str, Any]:
        assert len(v) == 1
        return v


def unpack(d: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    type = next(iter(d.keys()))
    kwargs = values if (values := next(iter(d.values()))) is not None else dict()
    return type, kwargs


@dataclass
class BuildConfig:
    _file: Path

    def __post_init__(self) -> None:
        with open(self._file) as f:
            loaded = yaml.safe_load(f)
            print(loaded)
        # check the parsed dict here
        self.d = BuildData(**loaded)

    @property
    def name(self) -> str:
        return self.d.name

    @property
    def specialization(self) -> Gunner | None:
        type, kwargs = unpack(self.d.specialization)
        match type:
            case 'Gunner':
                return Gunner(**kwargs)
            case _:
                return None

    @property
    def dict(self) -> dict[str, Any]:
        return dict(
            name=self.name,
            specialization=self.specialization,
        )
