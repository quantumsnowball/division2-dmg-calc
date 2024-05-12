from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import Any, Self, Sequence

import yaml


class Float(float):
    def __new__(cls,
                x: float,
                src: Sequence[str] | None = None) -> Self:
        # it is a normal float
        self = super().__new__(cls, x)
        # add meta data
        self._src = src if src is not None else []
        # return self
        return self

    @property
    def src(self) -> list[str]:
        ''' list of str meta data, suppose to record stats source '''
        return self._src

    @src.setter
    def src(self, val: list[str]) -> None:
        # only list[str] could be set to this property
        assert all(isinstance(v, str) for v in val)
        self._src = val

    def __add__(self, other: float | Float) -> Float:
        ''' preserve the src when add to another float|Float '''
        result = super().__add__(other)
        if isinstance(other, Float):
            self.src += other.src
        return Float(result, self.src)


def dataclass_asdict(dc: Any) -> dict[str, Any]:
    '''
    try to convert the dataclass instance into a dict,
    ignoring any known circular reference
    '''
    CIRCULAR_FIELDS = ('_gears', )
    d = {}
    # only handle dataclass fields
    for f in fields(dc):
        # ignore any known circular fields
        if f.name in CIRCULAR_FIELDS:
            continue
        # read field value
        val = getattr(dc, f.name)
        # nest one level if a field itself is a dataclass
        if is_dataclass(val):
            val = dataclass_asdict(val)
        elif isinstance(val, (tuple, list)):
            val = [dataclass_asdict(itm)
                   if is_dataclass(itm)
                   else itm
                   for itm in val]
        # assign
        d[f.name] = val
    # result
    package = {type(dc).__name__: d}
    return package


def build_as_yaml(build: Any) -> str:
    dc_dict = dataclass_asdict(build)
    yaml_str = yaml.dump(dc_dict, sort_keys=False)
    return yaml_str


def pformat_dataclass(dc: Any, level: int = 1, indent: int = 4) -> str:
    SKIPPED_FIELDS = (
        '_gears',
        'bonus_pool',
    )
    SPACE = ' '
    s = type(dc).__name__
    fs = fields(dc)
    for f in fs:
        # ignore any known circular fields
        if f.name in SKIPPED_FIELDS:
            continue
        # read field value
        val = getattr(dc, f.name)
        # indent format
        if len(fs) > 1:
            field_name_text = f'{SPACE*indent*level}{f.name}'
            if level <= 1:
                s += '\n'
            s += f'\n{field_name_text:35s} | '
        else:
            s += '('
        # display format base on types
        if is_dataclass(val):
            val = pformat_dataclass(val, level+1, indent)
            s += val
        elif isinstance(val, (tuple, list)):
            for v in val:
                s += '\n'
                s += ' ' * indent * (level+1)
                s += '- '
                val = pformat_dataclass(v, level+2, indent)
                s += val
        elif isinstance(val, str):
            s += f"'{val}'"
        else:
            s += str(val)
        # format
        if len(fs) <= 1:
            s += ')'

    return s
