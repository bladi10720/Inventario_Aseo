# Inventario de aseo (Streamlit + Postgres)

App web sencilla para controlar **implementos de aseo**: entradas, salidas diarias, inventario, alertas de bajo stock y catálogo de productos.

Un solo **PIN de acceso** para todo el equipo (sin roles ni administrador).

## Requisitos

- Python 3.12+
- Base de datos Postgres (recomendado: Neon u otra instancia)

## Variables de entorno

- `DATABASE_URL`: connection string Postgres (ej. con `sslmode=require` en Neon)
- `ACCESS_PIN`: PIN único para entrar a la app

## Ejecutar local

```bash
python -m pip install -r requirements.txt
```

PowerShell:

```powershell
$env:DATABASE_URL="postgresql://..."
$env:ACCESS_PIN="1234"
python -m streamlit run app.py
```

## Primera vez

1. Entra con el PIN.
2. Menú **Productos** → **Inicializar base de datos**.
3. Importa `Productos.csv` o agrega productos manualmente.

## Despliegue (Streamlit Cloud + Neon)

1. Sube este repo a GitHub (proyecto separado de Inventario Shell).
2. Crea una base de datos **nueva** en Neon (no reutilices la de Shell).
3. Despliega en Streamlit Community Cloud.
4. Secrets:
   - `DATABASE_URL`
   - `ACCESS_PIN`
5. Inicializa tablas e importa productos desde la app.

## Menú

| Pantalla | Uso |
|----------|-----|
| Entradas | Compras / reposición |
| Salidas diarias | Consumo o entrega del día |
| Inventario | Consulta de stock |
| Alertas | Stock bajo (< 2) |
| Productos | Alta, CSV, edición |
| Ajuste de stock | Conteo físico |
