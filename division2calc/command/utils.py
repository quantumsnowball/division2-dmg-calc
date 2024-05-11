from pathlib import Path

import pandas as pd

from division2calc.build.common import Metric, Profile
from division2calc.utils import load_builds_file


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
