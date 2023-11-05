from typeguard import typechecked
from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum


class LoggingLevel(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"


class CustomField:
    format: Optional[str] = None
    title: str
    default: Optional[str] = None
    required: bool = False


@typechecked
@dataclass
class Info:
    order: Optional[List[str]] = None
    custom: List[CustomField] = field(default_factory=list)


@typechecked
@dataclass
class Aliases:
    downgrade: Optional[str] = None
    upgrade: Optional[str] = None


@typechecked
@dataclass
class Revision:
    aliases: Aliases = field(default_factory=Aliases)
    info: Info = field(default_factory=Info)


@typechecked
@dataclass
class SourceInfo:
    directory: str = "./versions"


@typechecked
@dataclass
class Source:
    type: str = "VersionsDirectory"
    info: SourceInfo = field(default_factory=SourceInfo)


@typechecked
@dataclass
class Logging:
    level: LoggingLevel = LoggingLevel.INFO
    with_trace: bool = False


@typechecked
@dataclass
class Configuration:
    revision: Revision = field(default_factory=Revision)
    source: Source = field(default_factory=Source)
    logging: Logging = field(default_factory=Logging)
