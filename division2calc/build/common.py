from typing import Literal, get_args


Metric = Literal['stats', 'damage', 'x', 'dydx']
Profile = Literal['basic', 'min', 'average', 'max']
Profiles = tuple[Profile]
SortOrder = Literal['asc', 'desc']
SortBy = tuple[str, SortOrder]

PROFILES: Profiles = get_args(Profile)
