from dataclasses import dataclass

import gear.attrs as attrs
import gear.brandsets.bonus as bonus


@dataclass(kw_only=True)
class Brandsets:
    brandset: str
    attr2: attrs.MinorAttribute
    # bonus1pc: bonus.Bonus
    # bonus2pc: bonus.Bonus
    # bonus3pc: bonus.Bonus
