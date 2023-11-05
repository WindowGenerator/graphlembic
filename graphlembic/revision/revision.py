from __future__ import annotations
import re

from typeguard import typechecked
from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Iterator
from graphlembic.errors import GraphlembicRevisionError

# RevisionHash = _Alias[str]

__NOT_SETTED_OBJECT = object()
REVISION_ID_PATTERN = re.compile(r"^[a-z0-9]+$")


def validate_revsion_id(id: str) -> None:
    if len(id) != 12:
        raise GraphlembicRevisionError(id, "Revision ID must contains 12 symbols")
    if REVISION_ID_PATTERN.match(id) is None:
        raise GraphlembicRevisionError(
            id,
            "Revision ID must contains only lower ascii chars 'a-z' and numbers '0-9'",
        )


class RevisionID(str):
    def __init__(self, id: str) -> None:
        validate_revsion_id(id)
        super().__init__(self, id)


class Revisions:
    def __init__(self) -> None:
        self._revisions: Dict[RevisionID, Revision] = dict()

    def add_revision(self, rev: Revision) -> None:
        ...

    def add_next_revision(
        self, revision: RevisionID, next_revision: RevisionID
    ) -> None:
        ...

    def __iter__(self) -> Iterator[Revision]:
        ...

    def __next__(self) -> Revision:
        ...


@typechecked
@dataclass
class RevisionInfo:
    message: Optional[str] = None
    description: Optional[str] = None
    cur_revision: RevisionID  # This should be provided when creating an instance
    prev_revision: Optional[RevisionID] = None
    create_date: date  # This should be provided when creating an instance
    custom_fields: Optional[Dict[str, str]] = None


class MetaRevisionInfo:
    def __init__(self, revision_info: RevisionInfo) -> None:
        self._info = revision_info
        self._cur_revision = revision_info.cur_revision
        self._prev_revision = revision_info.prev_revision
        self._next_revision = __NOT_SETTED_OBJECT

    @property
    def info(self) -> RevisionInfo:
        return self._info

    @property
    def next_revision(self) -> Optional[RevisionID]:
        return (
            self._next_revision
            if self._next_revision is not __NOT_SETTED_OBJECT
            else None
        )

    @property.setter
    def next_revision(self, revision: Optional[RevisionID]) -> None:
        if self._next_revision is not __NOT_SETTED_OBJECT:
            raise GraphlembicRevisionError(
                self._cur_revision, "This reversion already has been setted"
            )

        self._next_revision = revision

    def is_head(self) -> bool:
        return self._next_revision is None

    def is_base(self) -> bool:
        return self._prev_revision is None

    def __hash__(self) -> str:
        return self._cur_revision


class Revision:
    def __init__(
        self, meta_revision_info: MetaRevisionInfo, upgrade, downgrade
    ) -> None:
        self._meta_revision_info = meta_revision_info

    @property
    def revision_info(self) -> RevisionInfo:
        return self._meta_revision_info
