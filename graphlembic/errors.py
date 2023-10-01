from typing import List, Optional
from pathlib import Path


class GraphlembicErrorMixin:
    def __init__(self, details: Optional[List[str]] = None) -> None:
        self._details = details if details is not None else []
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, Details: [{', '.join(self._details)}]"
    
    def __str__(self) -> str:
        return self.__repr__()


class GraphlembicRevisionError(GraphlembicErrorMixin, Exception):
    def __init__(self, revesion: str, message: str) -> None:
        super().__init__([f"Reversion: {revesion}", f"Error message: {message}"])


class GraphlembicImportError(GraphlembicErrorMixin, ImportError):
    def __init__(self, message: str, path: Path) -> None:
        super().__init__([f"Path: {path}", f"Error message: {message}"])