from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

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
