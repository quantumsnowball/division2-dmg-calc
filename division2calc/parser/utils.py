from pathlib import Path

import click


class BuildYAMLPathParamType(click.ParamType):
    name = 'BuildYAMLPath'

    def convert(self,
                value: str,
                param: click.Parameter | None,
                ctx: click.Context | None) -> Path:
        return Path(value)
