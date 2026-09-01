from __future__ import annotations

import streamlit as st

from src.auth import logout_button, require_auth
from src.config import load_settings
from src.ui.branding import APP_DISPLAY_NAME, apply_mobile_app_name


def main() -> None:
    st.set_page_config(page_title=APP_DISPLAY_NAME, layout="wide")
    apply_mobile_app_name()

    settings = load_settings()
    require_auth(settings)

    st.sidebar.title("Inventario de aseo")
    logout_button()

    page = st.sidebar.radio(
        "Menú",
        options=[
            "Entradas",
            "Salidas diarias",
            "Inventario",
            "Alertas",
            "Productos",
            "Ajuste de stock",
        ],
    )

    if page == "Entradas":
        from src.ui.pages.entrada import render as render_entrada

        render_entrada()
    elif page == "Salidas diarias":
        from src.ui.pages.salida_diaria import render as render_salida

        render_salida()
    elif page == "Inventario":
        from src.ui.pages.inventario import render as render_inventario

        render_inventario()
    elif page == "Alertas":
        from src.ui.pages.alertas import render as render_alertas

        render_alertas()
    elif page == "Productos":
        from src.ui.pages.productos import render as render_productos

        render_productos()
    elif page == "Ajuste de stock":
        from src.ui.pages.ajuste_stock import render as render_ajuste

        render_ajuste()
    else:
        st.write("Selecciona una opción del menú.")


if __name__ == "__main__":
    main()
