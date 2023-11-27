from graphlembic.revisions.parsers.base import ParsingSourceStrategy
from graphlembic.revisions.revision import Revisions
from graphlembic.config.model import CQLSourceInfo


class CQLSourceParserStrategy(ParsingSourceStrategy):
    def parse(self, source: CQLSourceInfo) -> Revisions:
        ...
