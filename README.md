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

### 1. Base de datos en Neon

1. Entra en [neon.tech](https://neon.tech) y crea un proyecto nuevo.
2. Copia el **connection string** de Postgres (formato `postgresql://...`).
3. Si el string usa `postgres://`, cámbialo a `postgresql://`.
4. Añade `?sslmode=require` al final si no está.

### 2. Subir el código a GitHub

```powershell
cd c:\PROYECTOS\Inventario_Aseo
git remote add origin https://github.com/TU_USUARIO/Inventario_Aseo.git
git push -u origin main
```

(Crea el repositorio vacío en GitHub antes del `push`.)

### 3. Desplegar en Streamlit Cloud

1. Entra en [share.streamlit.io](https://share.streamlit.io) con tu cuenta de GitHub.
2. **New app** → elige el repo `Inventario_Aseo`, rama `main`, archivo `app.py`.
3. En **Advanced settings → Secrets**, pega:

```toml
DATABASE_URL = "postgresql://usuario:password@host/db?sslmode=require"
ACCESS_PIN = "tu-pin-seguro"
```

4. **Deploy**.

### 4. Primera vez en producción

1. Abre la URL de la app e ingresa el PIN.
2. **Productos** → **Inicializar base de datos**.
3. Importa `Productos.csv` o agrega productos manualmente.

## Menú

| Pantalla | Uso |
|----------|-----|
| Entradas | Compras / reposición |
| Salidas diarias | Consumo o entrega del día |
| Inventario | Consulta de stock |
| Alertas | Stock bajo (< 2) |
| Productos | Alta, CSV, edición |
| Ajuste de stock | Conteo físico |
