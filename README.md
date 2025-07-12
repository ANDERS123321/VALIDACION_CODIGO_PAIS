# 📱 Validador de Números Celulares (Perú e Internacionales)

Este es un proyecto en Python que permite validar números celulares del **Perú** y de otros países con formato internacional. Incluye una interfaz web simple, pruebas automáticas y una configuración para integración continua con GitHub Actions.

---

## 🗂️ Estructura del Proyecto

```
prueba/
├── app.py                       # Servidor Flask para validar números
├── index.html                   # Interfaz web básica
├── requirements.txt             # Dependencias del proyecto
├── .gitignore
├── .github/workflows/ci.yml     # Configuración de CI (pytest)
├── src/
│   └── validador.py             # Lógica principal de validación
├── tests/
│   └── test_validador.py        # Pruebas unitarias
```

---

## 🚀 Características

- ✅ Validación de números celulares de Perú (`+51`, `9xxxxxxxx`)
- 🌍 Soporte para números internacionales con código `+`
- 🧪 Pruebas automáticas con `pytest`
- 🌐 Interfaz web con HTML + Flask
- 🔁 Integración continua con GitHub Actions

---

## ▶️ Ejecución del Proyecto

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la app

```bash
python app.py
```

Abre el navegador en [http://localhost:5000](http://localhost:5000)

---

## 🧪 Ejecutar Pruebas

```bash
pytest o python -m pytest
```

---

## 🌍 Ejemplos de Números Válidos

| Número              | País       | Válido |
|---------------------|------------|--------|
| `+51912345678`      | Perú       | ✅     |
| `912345678`         | Perú       | ✅     |
| `+14155552671`      | EE.UU.     | ✅     |
| `123456`            | Inválido   | ❌     |

---

## ⚙️ CI con GitHub Actions

Este proyecto incluye un flujo de trabajo (`.github/workflows/ci.yml`) que ejecuta los tests automáticamente cuando se hacen cambios en el repositorio.

---

## 📄 Licencia

Este proyecto es de código abierto bajo la licencia MIT.
