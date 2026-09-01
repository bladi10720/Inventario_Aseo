from __future__ import annotations

import streamlit as st

from .config import Settings

_SESSION_KEY = "access_granted"


def is_authenticated() -> bool:
    return bool(st.session_state.get(_SESSION_KEY))


def require_auth(settings: Settings) -> None:
    if is_authenticated():
        return

    st.title("Inventario de aseo")
    st.subheader("Acceso")
    pin = st.text_input("PIN", type="password")

    if st.button("Entrar", type="primary"):
        if (pin or "").strip() == settings.access_pin:
            st.session_state[_SESSION_KEY] = True
            st.rerun()
        else:
            st.error("PIN incorrecto.")

    st.stop()


def logout_button() -> None:
    if st.sidebar.button("Cerrar sesión"):
        st.session_state.pop(_SESSION_KEY, None)
        st.rerun()
