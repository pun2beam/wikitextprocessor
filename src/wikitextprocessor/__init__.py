from __future__ import annotations

import os
import sys

from .common import MAGIC_FIRST, MAGIC_LAST
from .core import Page, TemplateArgs, Wtp
from .parser import HTMLNode, LevelNode, NodeKind, TemplateNode, WikiNode

__all__ = (
    "Wtp",
    "HTMLNode",
    "LevelNode",
    "NodeKind",
    "TemplateNode",
    "WikiNode",
    "MAGIC_FIRST",  # Some applications with to use the same ranges
    "MAGIC_LAST",
    "Page",
    "TemplateArgs",
)

if os.environ.get("WTP_DEBUG_IMPORT"):
    print(
        "[wikitextprocessor] imported __init__ from",
        __file__,
        "(python",
        ".".join(map(str, sys.version_info[:3])),
        ")",
        flush=True,
    )
