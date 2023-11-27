from abc import abstractmethod, ABC
from graphlembic.revisions.revision import Revisions
from graphlembic.config.model import Sources


class ParsingSourceStrategy(ABC):
    @abstractmethod
    def parse(self, source: Sources) -> Revisions:
        ...
