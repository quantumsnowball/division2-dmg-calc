from dataclasses import fields, is_dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Any

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
