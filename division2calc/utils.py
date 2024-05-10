from dataclasses import fields, is_dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Any, Iterable, Sequence

import yaml

from division2calc.build import Build


def load_build_file(file: Path,
                    name: str = 'build') -> Build:
    # spec
    spec = spec_from_file_location(name, Path(file))
    assert spec and spec.loader, f'Failed to load module: {file=} {name=}'
    # module
    module = module_from_spec(spec)
    # load the module
    spec.loader.exec_module(module)
    # should be a build var
    build: Build = module.build
    # result
    return build


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


def build_as_yaml(build: Build) -> str:
    dc_dict = dataclass_asdict(build)
    yaml_str = yaml.dump(dc_dict, sort_keys=False)
    return yaml_str


def pformat_dataclass(dc: Any, level: int = 1, indent: int = 4) -> str:
    CIRCULAR_FIELDS = ('_gears', )
    SKIPPED_FIELDS = ('bonus_pool', )
    s = type(dc).__name__
    for f in fields(dc):
        # ignore any known circular fields
        if f.name in CIRCULAR_FIELDS or f.name in SKIPPED_FIELDS:
            continue
        s += '\n'
        s += ' ' * indent * level
        s += f'{f.name}: '
        # read field value
        val = getattr(dc, f.name)
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

            pass
        elif isinstance(val, str):
            s += f"'{val}'"
        else:
            s += str(val)

    # s += ' ' * indent * (level-1) + ')'

    return s
