from __future__ import annotations

from abc import abstractmethod
from types import ModuleType
from typing import Optional
from pathlib import Path
from graphlembic.helpers.loader import load_python_file


class MigraionScriptBase:
    @abstractmethod
    def parse(self) -> MigraionScriptBase:
        ...


class MigraionScript:
    def __init__(self, directory: Path, filename: Path) -> None:
        self._directory = directory
        self._filename = filename
        self._module: Optional[ModuleType] = None

    def open(self) -> MigraionScript:
        self._module = load_python_file(self._directory, self._filename)

        return self

    def parse(self) -> MigraionScript:
        ...

    def upgrade(self) -> None:
        ...

    def downgrade(self) -> None:
        ...

    def get_description(self) -> str:
        ...
