from __future__ import annotations

from graphlembic.config import Configuration


class EnviromentCtxBase:
    def __init__(self, config: Configuration) -> None:
        self._config = config

    def __enter__(self) -> EnviromentCtxBase:
        return self
    
    def __exit__(self) -> None:
        ...