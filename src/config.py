from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    database_url: str
    access_pin: str


def _read_setting(name: str) -> str:
    value = os.getenv(name, "").strip()
    if value:
        return value
    try:
        import streamlit as st

        if name in st.secrets:
            return str(st.secrets[name]).strip()
    except Exception:
        pass
    return ""


def load_settings() -> Settings:
    database_url = _read_setting("DATABASE_URL")
    access_pin = _read_setting("ACCESS_PIN")

    if not database_url:
        raise RuntimeError("Missing required setting: DATABASE_URL")
    if not access_pin:
        raise RuntimeError("Missing required setting: ACCESS_PIN")

    return Settings(database_url=database_url, access_pin=access_pin)
