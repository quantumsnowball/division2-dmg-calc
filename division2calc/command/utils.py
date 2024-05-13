from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Sequence

import pandas as pd

from division2calc.build import Build
from division2calc.build.common import Metric, Profile


def load_builds_file(file: Path,
                     name: str = 'builds') -> Sequence[Build]:
    # spec
    spec = spec_from_file_location(name, Path(file))
    assert spec and spec.loader, f'Failed to load module: {file=} {name=}'
    # module
    module = module_from_spec(spec)
    # load the module
    spec.loader.exec_module(module)
    # should be a build var
    builds: Sequence[Build] = module.builds
    # result
    return builds


def load_builds_metric(file: Path,
                       metric: Metric,
                       profile: Profile) -> pd.DataFrame:
    # load builds
    builds = load_builds_file(file)
    # data
    data = {b.name: getattr(b.summary, metric).loc[profile]
            for b in builds}
    df = pd.DataFrame.from_dict(data, orient='index')
    # index names
    df.index.names = ('build name',)
    df.columns.names = [f'[{profile}] {metric}', ] + ['']*(df.columns.nlevels-1)
    # result
    return df
