from __future__ import annotations

from graphlembic.revision.revision import RevisionID
from pydantic import BaseModel
from datetime import date

class SystemNode(BaseModel):
    revision_id: RevisionID
    created_date: date
    message: str

__SYSTEM_NODE_NAME = "_SYSTEM_NODE"

class SystemNodeRepository:
    def __init__(self, tx) -> None:
        self._tx = tx
    
    def __enter__(self) -> SystemNodeRepository:
        return self

    def __exit__(self) -> None:
        ...
    
    def get_revision(self) -> RevisionID:
        sn = self.get()
        return sn.revision_id

    def set(self, sn: SystemNode) -> None:
        ...
    
    def get(self) -> SystemNode:
        ...
