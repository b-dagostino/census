from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from email.message import Message
from typing import Any, ClassVar, Self, Type, TYPE_CHECKING

import requests
from pydantic import AnyUrl


@dataclass
class ContentType:
    media_type: str
    parameters: dict[str, str]

    _CONTENT_TYPE: ClassVar[str] = "content-type"
    _JSON_CONTENT_TYPE: ClassVar[str] = "application/json"

    # Inspired from https://stackoverflow.com/a/75727619
    @classmethod
    def from_str(cls: Type[Self], content_type: str) -> Self:
        m = Message()
        m[cls._CONTENT_TYPE] = content_type
        params = m.get_params()
        return cls(params[0][0], dict(params[1:]))  # type: ignore[index]

    @classmethod
    def from_response(cls: Type[Self], r: requests.Response) -> Self:
        return cls.from_str(r.headers[cls._CONTENT_TYPE])

    @property
    def is_json(self) -> bool:
        return self.media_type == self._JSON_CONTENT_TYPE


def get_json_from_url(url: str | AnyUrl) -> dict:
    from json import loads
    r = requests.get(str(url))
    r.raise_for_status()

    content_type = ContentType.from_response(r)
    if not content_type.is_json:
        raise ValueError(f"Response not JSON: got {content_type.media_type}")

    return loads(r.text)


def hasattr(o: object, name: str | Sequence[str]) -> bool:
    from builtins import hasattr as hasattr_builtin

    if isinstance(name, str) or not isinstance(name, Sequence):
        return hasattr_builtin(o, name)

    if not name:
        return False

    head = name[0]

    if not hasattr_builtin(o, head):
        return False

    if len(name) > 1:
        return hasattr(getattr(o, head), name[1:])
    else:
        return True


def getattr(o: object, name: str | Sequence[str]) -> Any:
    from builtins import getattr as getattr_builtin

    if isinstance(name, str) or not isinstance(name, Sequence):
        return getattr_builtin(o, name)

    if not name:
        raise ValueError("name cannot be an empty sequence")

    head = name[0]

    if len(name) > 1:
        return getattr(getattr_builtin(o, head), name[1:])
    else:
        return getattr_builtin(o, head)

def make_identifer(id: str) -> str:
    from re import sub
    return sub(r"__+", "_", sub(r"\W|^\d", "_", id)).rstrip("_")

def RecursiveDefaultDict(): return defaultdict(RecursiveDefaultDict)