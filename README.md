# 🚀 FastAPI Simple Project - Cursor IDE Course

Este proyecto es parte del curso de **Cursor IDE**, un editor de código potenciado por IA que mejora la productividad del desarrollador. El proyecto demuestra las mejores prácticas para desarrollar APIs RESTful usando FastAPI y Python.

## 📋 Descripción del Proyecto

**FastAPI Simple** es una aplicación web que implementa una API REST para gestionar un menú de restaurante. El proyecto está diseñado para enseñar los conceptos fundamentales de FastAPI, incluyendo:

- Creación de endpoints REST
- Validación de datos con Pydantic
- Manejo de errores HTTP
- Middleware CORS
- Operaciones CRUD completas
- Documentación automática de API

## ✨ Características Principales

- **API RESTful** con endpoints para gestión de platos
- **Validación automática** de datos usando Pydantic
- **Documentación automática** con Swagger UI
- **Middleware CORS** configurado
- **Manejo de errores** robusto
- **Base de datos en memoria** para demostración
- **Estructura modular** siguiendo mejores prácticas

## 🏗️ Estructura del Proyecto

```
fastapi-simple/
├── main.py              # Aplicación principal FastAPI
├── models/              # Modelos Pydantic
│   └── plato.py        # Modelo para entidad Plato
├── settings.py          # Configuración de la aplicación
├── pyproject.toml       # Dependencias y metadatos del proyecto
├── uv.lock             # Lock file de dependencias
└── .python-version     # Versión de Python
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.12 o superior
- UV (gestor de paquetes Python moderno)

### Pasos de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd cursor-course/fastapi-simple
   ```

2. **Instalar dependencias:**
   ```bash
   uv sync
   ```

3. **Ejecutar la aplicación:**
   ```bash
   uv run uvicorn main:app --reload
   ```

4. **Acceder a la aplicación:**
   - API: http://localhost:8000
   - Documentación: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 📚 Endpoints de la API

### Endpoints Básicos

- `GET /` - Mensaje de bienvenida
- `GET /health` - Verificación de estado de salud
- `GET /users` - Lista de usuarios
- `POST /users` - Crear nuevo usuario

### Endpoints CRUD para Platos

- `POST /platos` - Crear nuevo plato
- `GET /platos` - Obtener todos los platos
- `GET /platos/{plato_id}` - Obtener plato específico
- `PUT /platos/{plato_id}` - Actualizar plato existente
- `DELETE /platos/{plato_id}` - Eliminar plato

## 🍽️ Modelo de Datos

### Plato

```python
class Plato(BaseModel):
    id: str          # Identificador único (UUID)
    name: str        # Nombre del plato
    precio: float    # Precio (debe ser mayor a 0)
```

## 🛠️ Tecnologías Utilizadas

- **FastAPI** - Framework web moderno y rápido para APIs
- **Pydantic** - Validación de datos y serialización
- **Uvicorn** - Servidor ASGI de alto rendimiento
- **UV** - Gestor de paquetes Python moderno
- **Python 3.12** - Versión más reciente de Python

## 📖 Uso de la API

### Crear un Nuevo Plato

```bash
curl -X POST "http://localhost:8000/platos" \
     -H "Content-Type: application/json" \
     -d '{"name": "Pizza Margherita", "precio": 15.99}'
```

### Obtener Todos los Platos

```bash
curl "http://localhost:8000/platos"
```

### Actualizar un Plato

```bash
curl -X PUT "http://localhost:8000/platos/{plato_id}" \
     -H "Content-Type: application/json" \
     -d '{"name": "Pizza Margherita", "precio": 18.99}'
```

## 🔧 Configuración

El archivo `settings.py` contiene la configuración de la aplicación:

- Nombre del proyecto
- Versión
- Descripción
- Hosts permitidos para CORS
- Configuraciones adicionales

## 📚 Aprendizaje con Cursor IDE

Este proyecto está diseñado para aprovechar las capacidades de **Cursor IDE**:

- **Autocompletado inteligente** para código Python y FastAPI
- **Generación de código** asistida por IA
- **Refactoring automático** y sugerencias de mejora
- **Debugging avanzado** con herramientas integradas
- **Integración Git** para control de versiones

## 🧪 Próximos Pasos

- [ ] Implementar base de datos persistente (PostgreSQL/SQLite)
- [ ] Agregar autenticación y autorización
- [ ] Implementar tests unitarios y de integración
- [ ] Agregar logging y monitoreo
- [ ] Implementar cache con Redis
- [ ] Despliegue en contenedores Docker

## 🤝 Contribución

Este es un proyecto educativo del curso de Cursor IDE. Las contribuciones son bienvenidas para mejorar el aprendizaje y la funcionalidad.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**Desarrollado con ❤️ usando Cursor IDE para el aprendizaje de FastAPI y desarrollo de APIs modernas.**
