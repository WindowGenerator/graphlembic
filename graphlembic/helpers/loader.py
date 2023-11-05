from __future__ import annotations

import os
import importlib
import re
from pathlib import Path
from typing import Optional, Any, _Alias
from graphlembic.errors import GraphlembicImportError

Module = _Alias[Any]


def load_python_file(directory: Path, filename: Path) -> Module:
    """Load a file from the given path as a Python module."""

    module_id = re.sub(r"\W", "_", filename)
    path = directory / filename
    _, ext = os.path.splitext(filename)

    if not path.exists():
        raise GraphlembicImportError("Path doesn't exist", path)

    if not path.is_dir():
        raise GraphlembicImportError("Path is directrory", path)

    if ext == ".py":
        if os.path.exists(path):
            module = load_py_module(module_id, path)
        else:
            pyc_path = pyc_file_from_path(path)

            if pyc_path is None:
                raise GraphlembicImportError("Can't find Python file", path)

            module = load_py_module(module_id, pyc_path)
    elif ext in (".pyc", ".pyo"):
        module = load_py_module(module_id, path)
    else:
        raise GraphlembicImportError("Can't find Python file", path)

    return module


def pyc_file_from_path(path: Path) -> Optional[str]:
    """Given a python source path, locate the .pyc."""

    candidate = importlib.util.cache_from_source(path)
    if path.exists(candidate):
        return candidate


def load_py_module(module_id: str, path: str) -> Module:
    spec = importlib.util.spec_from_file_location(module_id, path)
    assert spec
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
