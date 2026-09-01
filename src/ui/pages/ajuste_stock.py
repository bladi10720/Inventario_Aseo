from __future__ import annotations

from datetime import date

import streamlit as st

from ...db import get_engine
from ...repo.movements import ACTOR_ROLE, get_stock_by_code, insert_movement
from ...repo.products import get_product


def render() -> None:
    st.header("Ajuste de stock")
    st.caption("Corrige el stock tras un conteo físico.")
    engine = get_engine()

    if st.session_state.pop("_reset_adj_widgets", False):
        st.session_state["adj_code"] = ""
        st.session_state["adj_date"] = date.today()

    col1, col2 = st.columns([2, 1])
    with col1:
        code = st.text_input("Código", key="adj_code", placeholder="Ej: 001")
    with col2:
        movement_date = st.date_input("Fecha", key="adj_date", value=date.today())

    code_norm = (code or "").strip()
    if not code_norm:
        st.info("Ingresa un código para ver el stock actual y ajustar.")
        return

    product = get_product(engine=engine, code=code_norm)
    if not product:
        st.error("El código no existe en productos.")
        return

    current_stock = get_stock_by_code(engine=engine, code=code_norm) or 0
    st.success(f"{product.name} — {product.category}")
    st.metric("Stock actual", int(current_stock))

    st.subheader("Nuevo stock")
    new_stock = st.number_input("Stock correcto (conteo físico)", min_value=0, step=1, value=int(current_stock))

    reason = st.text_input("Motivo (obligatorio)", placeholder="Ej: Conteo físico / Merma")

    delta = int(new_stock) - int(current_stock)
    if delta == 0:
        st.info("No hay diferencia. No se creará ningún movimiento.")
        return

    st.caption(f"Diferencia: {delta:+d} (se registrará como {'ENTRADA' if delta > 0 else 'SALIDA'})")

    if st.button("Registrar ajuste", type="primary"):
        if not reason.strip():
            st.error("El motivo es obligatorio.")
            return

        note = f"AJUSTE | Motivo: {reason.strip()} | Stock {int(current_stock)} -> {int(new_stock)}"
        movement_type = "IN" if delta > 0 else "OUT"
        qty = abs(int(delta))
        try:
            insert_movement(
                engine=engine,
                movement_type=movement_type,
                movement_date=movement_date,
                product_code=code_norm,
                qty=qty,
                actor_role=ACTOR_ROLE,
                note=note,
            )
            updated_stock = get_stock_by_code(engine=engine, code=code_norm) or 0
            st.success(f"Ajuste registrado. Nuevo stock: {int(updated_stock)}")
            st.session_state["_reset_adj_widgets"] = True
            st.rerun()
        except Exception as e:  # noqa: BLE001
            st.error(f"No se pudo registrar el ajuste: {e}")
