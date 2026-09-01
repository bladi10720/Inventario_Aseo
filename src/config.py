from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    database_url: str
    access_pin: str


def load_settings() -> Settings:
    database_url = os.getenv("DATABASE_URL", "").strip()
    access_pin = os.getenv("ACCESS_PIN", "").strip()

    if not database_url:
        raise RuntimeError("Missing required env var: DATABASE_URL")
    if not access_pin:
        raise RuntimeError("Missing required env var: ACCESS_PIN")

    return Settings(database_url=database_url, access_pin=access_pin)
