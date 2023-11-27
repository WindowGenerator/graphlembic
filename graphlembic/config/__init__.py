from graphlembic.config.model import Configuration
from pathlib import Path
import json


def get_config(config_path: Path) -> Configuration:
    with config_path.open("r") as fd:
        return Configuration(
            **json.load(fd)
        )
