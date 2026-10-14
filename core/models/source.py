from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class Source(BaseModel):
    type: Literal["rss", "manual", "notion", "telegram", "scraper"] = "rss"
    name: str
    url: str | None = None
    external_id: str | None = None
