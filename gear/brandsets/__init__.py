from dataclasses import dataclass

import gear.attrs as attrs


@dataclass(kw_only=True)
class Brandsets:
    attr2: attrs.MinorAttribute
