# 🚓 Simulador de Alcoholemia Vial

Sistema desarrollado en **Python** como proyecto académico para la asignatura de **Introducción a la Programación**.

El programa simula un proceso de control de alcoholemia realizado a conductores, permitiendo registrar información, determinar sanciones automáticamente y generar reportes en PDF.

---

## 📋 Descripción

El sistema permite registrar conductores sometidos a una prueba de alcoholemia, evaluando automáticamente el nivel de alcohol detectado y aplicando las sanciones correspondientes.

Además, incorpora herramientas para administrar los registros almacenados mediante búsquedas, filtros, estadísticas y exportación de reportes.

---

## ✨ Características

- Registro de conductores.
- Validación de cédulas.
- Validación de placas vehiculares.
- Generación automática de ID único.
- Registro de fecha de creación.
- Almacenamiento persistente en JSON.
- Búsqueda por cédula o placa.
- Búsquedas parciales.
- Filtrado por nivel de embriaguez.
- Eliminación de registros.
- Estadísticas generales.
- Conteo de reincidencias.
- Exportación de conductor en PDF.
- Exportación de estadísticas en PDF.
- Exportación completa de registros en PDF.

---

## 📂 Estructura del Proyecto

```text
python-simulador-alcoholemia-vial/

├── core/
│   ├── backend.py
│   └── validators.py
│
├── data/
│   └── drivers.json
│
├── reports/
│   └── pdf_export.py
│
├── ui/
│   └── console.py
│
├── pdf/
│   └── Reportes generados
│
├── main.py
└── README.md
```

---

## ⚙️ Tecnologías Utilizadas

- Python 3
- JSON
- ReportLab
- Tabulate

---

## 🚀 Instalación

Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/python-simulador-alcoholemia-vial.git
```

Entrar al directorio:

```bash
cd python-simulador-alcoholemia-vial
```

Instalar dependencias:

```bash
pip install reportlab
pip install tabulate
```

---

## ▶️ Ejecución

Desde la raíz del proyecto:

```bash
python main.py
```

---

## 📊 Funcionalidades Principales

### Agregar conductor

Permite registrar:

- Cédula
- Placa vehicular
- Nivel de alcohol

El sistema calcula automáticamente:

- Estado del conductor
- Multa
- Sanción

---

### Buscar conductor

Permite localizar registros mediante:

- Cédula
- Placa

También admite coincidencias parciales.

---

### Filtrar registros

Filtrado por:

- Embriaguez ligera
- Embriaguez
- Embriaguez extrema

---

### Estadísticas

Genera información como:

- Total de conductores registrados.
- Cantidad por tipo de embriaguez.
- Reincidencias.
- Distribución de sanciones.

---

### Exportación PDF

Permite generar:

- Reporte individual de conductor.
- Reporte estadístico.
- Tabla completa de registros.

---

## 📸 Capturas

### Menú principal

*(Insertar captura aquí)*

### Registro de conductor

*(Insertar captura aquí)*

### Tabla de registros

*(Insertar captura aquí)*

### Estadísticas

*(Insertar captura aquí)*

### Reportes PDF

*(Insertar captura aquí)*

---

## 🎓 Objetivo Académico

Este proyecto fue desarrollado con el objetivo de aplicar conceptos fundamentales de programación, incluyendo:

- Variables.
- Funciones.
- Condicionales.
- Ciclos.
- Validación de datos.
- Manejo de archivos.
- Organización modular del código.

---

## 📄 Licencia

Proyecto desarrollado con fines educativos y académicos.
