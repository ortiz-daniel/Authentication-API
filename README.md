# Authentication API

## Instalación de Dependencias

### 1. Clonar el repositorio

```bash
git clone https://tu-repositorio.git
```

### 2. Crear un entorno virtual (recomendado)

Un entorno virtual te permite aislar las dependencias de tu proyecto y evitar conflictos con otras instalaciones de Python.

#### Crear un entorno virtual con `venv` en Linux/macOS

```bash
python -m venv venv
source venv/bin/activate  # Para activar el entorno en Linux/macOS
```

#### Crear un entorno virtual con `venv` en Windows

```bash
python -m venv venv
venv\Scripts\activate  # Para activar el entorno en Windows
```

### 3. Instalar las dependencias

Una vez activado el entorno virtual, instala las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Explicación

- **Clonar el repositorio**: Este comando descarga el código fuente de tu proyecto desde tu repositorio de Git.
- **Crear un entorno virtual**: Un entorno virtual proporciona un espacio aislado para instalar paquetes de Python. Esto evita conflictos entre las versiones de los paquetes y mantiene tu entorno de desarrollo limpio.
- **Instalar dependencias**: El comando `pip install -r requirements.txt` lee el archivo `requirements.txt` que contiene una lista de los paquetes necesarios para tu proyecto y los instala en el entorno virtual activo.

## Ejecutando la aplicación con Docker Compose

### 1. Añadir un archivo de variables de entorno

Antes de iniciar el contenedor, asegúrate de añadir el archivo de variables de entorno a la raíz del proyecto con el siguiente comando (puedes crearlo manualmente):

```bash
touch .env.dev
```

Edita el archivo `.env.dev` para reemplazar los valores de las variables de entorno con los adecuados para tu entorno, fueron compartidos en el mail de entrega del proyecto.

### 2. Construir e iniciar los contenedores

Ejecuta el siguiente comando desde el directorio raíz de tu proyecto:

```bash
docker-compose up --build
```

Este comando hará lo siguiente:

- Construirá la imagen de Docker a partir del archivo `Dockerfile`.
- Iniciará los contenedores definidos en el archivo `docker-compose.yml`.

### 3. Acceder a la aplicación

Una vez que los contenedores estén en ejecución, podrás acceder a la documentación Swagger de la API en tu navegador web en la siguiente dirección:

```bash
http://localhost:3000/docs
```

## Ejecutando las Pruebas Unitarias

Para ejecutar las pruebas unitarias de la API, asegúrate de tener instalado el framework de pruebas que estés utilizando (por ejemplo, pytest). Luego, ejecuta el siguiente comando desde la raíz del repositorio:

```bash
pytest
```

### Personalizando la ejecución de pruebas

Si deseas ejecutar pruebas específicas, puedes utilizar las opciones de línea de comandos de pytest. Por ejemplo:

- **Ejecutar pruebas en un módulo específico:**

```bash
pytest tests/test_api.py
```

- **Ver el resultado en un formato más detallado:**

```bash
pytest -v
```
