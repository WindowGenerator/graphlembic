from graphlembic.revisions.parsers.base import ParsingSourceStrategy
from graphlembic.revisions.revision import Revisions
from graphlembic.config.model import PythonSourceInfo
from pathlib import Path
import os


class PythonSourceParserStratey(ParsingSourceStrategy):
    def parse(self, source: PythonSourceInfo) -> Revisions:
        revsions = Revisions()

        for os.path.:
            
