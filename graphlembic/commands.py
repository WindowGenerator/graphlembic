from graphlembic.revision.revision import RevisionID
from typing import Optional
from enum import Enum
from typeguard import typechecked


class Entites(Enum):
    ALL = "all"
    CONFIG = "config"
    REVISIONS = "revisions"


class Commands:
    """Define library API"""

    @typechecked
    def upgrade(self, to: Optional[RevisionID] = None) -> None:
        """
        Upgrade to RevisionID (if unset upgrade to head revision)
        """
        ...

    @typechecked
    def downgrade(self, to: Optional[RevisionID]) -> None:
        """
        Downgrade to RevisionID (if unset downgrade to base revision)
        """
        ...

    @typechecked
    def head(self) -> None:
        """
        Get head revision ID
        """
        ...

    @typechecked
    def base(self) -> None:
        """
        Get base revision ID
        """
        ...

    @typechecked
    def current(self) -> None:
        """
        Get current revision ID
        """
        ...

    @typechecked
    def history(self) -> None:
        """
        Get history like in git
        """
        ...

    @typechecked
    def update(self, version: Optional[str]) -> None:
        """
        Update tool to 'version' (if unset update to latest version)
        """
        ...

    @typechecked
    def validate(self, entity: Entites = Entites.ALL) -> None:
        """
        Validate 'config' or 'revisions' or 'all' (if unset validate 'all')
        """
        ...
