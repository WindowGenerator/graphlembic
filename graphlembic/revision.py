from __future__ import annotations

from typing import _Alias, Optional, Dict, Iterator
from graphlembic.errors import GraphlembicRevisionError

RevisionHash = _Alias[str]

__NOT_SETTED_OBJECT = object()


class Revisions:
    def __init__(self) -> None:
        self._revisions: Dict[RevisionHash, Revision] = dict()
    
    def validate(self) -> None:
        ...

    def add_revision(self, rev: Revision) -> None:
        ...
    
    def add_next_revision(self, revision: RevisionHash, next_revision: RevisionHash) -> None:
        ...
    
    def __iter__(self) -> Iterator[Revision]:
        ...
    
    def __next__(self) -> Revision:
        ...


class Revision:
    def __init__(self, cur_revision: RevisionHash, prev_revision: Optional[RevisionHash]) -> None:
        self._cur_revision = cur_revision
        self._prev_revision = prev_revision
        self._next_revision = __NOT_SETTED_OBJECT
    
    @property
    def next_revision(self) -> Optional[RevisionHash]:
        return self._next_revision if self._next_revision is not __NOT_SETTED_OBJECT else None

    @property.setter
    def next_revision(self, revision: Optional[RevisionHash]) -> None:
        if self._next_revision is not __NOT_SETTED_OBJECT:
            raise GraphlembicRevisionError(self._cur_revision, "This reversion already has been setted")
            
        self._next_revision = revision
    
    def is_head(self) -> bool:
        return self._next_revision is None
    
    def is_base(self) -> bool:
        return self._prev_revision is None

    def __hash__(self) -> str:
        return self._cur_revision

