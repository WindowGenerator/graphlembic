from pathlib import Path
from graphlembic.helpers.loader import load_python_file


class Script:
    def __init__(self, directory: Path, filename: Path) -> None:
        self._directory = directory
        self._filename = filename
        self._module = load_python_file(directory, filename)

    
    def upgrade() -> None:
        ...
    
    def downgrade() -> None:
        ...
    
    def get_description() -> str:
        ...
