from typing import Literal, get_args


Metric = Literal['stats', 'damage', 'x', 'dydx']
Metrics = tuple[Metric, ...]
Profile = Literal['basic', 'min', 'average', 'max']
Profiles = tuple[Profile, ...]
SortOrder = Literal['asc', 'desc']
SortOrders = tuple[SortOrder]
SortBy = tuple[str, SortOrder]

METRICS: Metrics = get_args(Metric)
PROFILES: Profiles = get_args(Profile)
SORT_ORDERS: SortOrders = get_args(SortOrder)
