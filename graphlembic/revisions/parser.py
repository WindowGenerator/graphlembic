from __future__ import annotations

from abc import abstractmethod
from types import ModuleType
from typing import Optional
from pathlib import Path
from graphlembic.helpers.loader import load_python_file
from graphlembic.config.model import Sources
from graphlembic.revisions.revision import Revisions



def parse(source: Sources) -> Revisions:
    ...
# class MigraionScriptBase:
#     @abstractmethod
#     def parse(self) -> MigraionScriptBase:
#         ...


# class MigraionScript:
#     def __init__(self, directory: Path, filename: Path) -> None:
#         self._directory = directory
#         self._filename = filename
#         self._module: Optional[ModuleType] = None

#     def parse(self) -> :
#         ...

#     def upgrade(self) -> None:
#         ...

#     def downgrade(self) -> None:
#         ...

#     def get_description(self) -> str:
#         ...
