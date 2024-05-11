from typing import Literal


Metric = Literal['damage', 'x', 'dydx']
Profile = Literal['basic', 'min', 'average', 'max']
SortOrder = Literal['asc', 'desc']
SortBy = tuple[str, SortOrder]
