from typing import Optional, List, Union, Literal
from enum import Enum

from pydantic import BaseModel, Field


class LoggingLevel(str, Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"

class SourceType(str, Enum):
    PYTHON_SCRIPTS = "PythonScripts"
    CQL_SCRIPTS = "CQLScripts"

class CustomField(BaseModel):
    format: Optional[str] = None
    title: str
    default: Optional[str] = None
    required: bool = False

class Info(BaseModel):
    order: Optional[List[str]] = None
    custom: List[CustomField] = Field(..., default_factory=list)

class Aliases(BaseModel):
    downgrade: Optional[str] = None
    upgrade: Optional[str] = None

class Revision(BaseModel):
    aliases: Aliases = Field(..., default_factory=Aliases)
    info: Info = Field(..., default_factory=Info)

class PythonSourceInfo(BaseModel):
    type: Literal["PythonSource"]
    directory: str


class CQLSourceDirectories(BaseModel):
    type: Literal["CQLSource"]
    root: str
    upgrade: str
    downgrade: str

class CQLSourceInfo(BaseModel):
    directories: CQLSourceDirectories


Sources = Union[PythonSourceInfo, CQLSourceInfo]

class Logging(BaseModel):
    level: LoggingLevel = LoggingLevel.INFO
    with_trace: bool = False

class Configuration(BaseModel):
    revision: Revision = Field(..., default_factory=Revision)
    source: Sources = Field(..., discriminator="type")
    logging: Logging = Field(..., default_factory=Logging)
