# Authentication API

## Instalación de Dependencias

### 1. Clonar el repositorio

```bash
git clone https://github.com/ortiz-daniel/Authentication-API.git
```

### 2. Crear un entorno virtual (recomendado)

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

## Ejecutando la aplicación con Docker Compose

### 1. Añadir un archivo de variables de entorno

Antes de iniciar el contenedor, asegúrate de añadir el archivo de variables de entorno a la raíz del proyecto con el siguiente comando (también puedes crearlo manualmente):

```bash
touch .env.dev
```

Edita el archivo `.env.dev` para reemplazar los valores de las variables de entorno con los adecuados para tu entorno, fueron compartidos en el mail de entrega del proyecto, simplemente copia y pega los valores.

### 2. Construir e iniciar los contenedores

Ejecuta el siguiente comando desde el directorio raíz del repositorio:

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

### 4. Consultando el primer endpoint

Para consultar el primer endpoint de la API, puedes utilizar el siguiente comando:

```bash
curl -X GET "http://localhost:3000/users" -H "accept: application/json" -H "Content-Type: application/json" -H 'accept: application/json' -d '{"email": "jonhdoe@mail.com", "password": "helloworld!"}'
```

## Ejecutando las Pruebas Unitarias

Para ejecutar las pruebas unitarias de la API, asegúrate de tener instalado el framework de pruebas: pytest.
Luego, ejecuta el siguiente comando desde la raíz del repositorio:

```bash
pytest
```

Si deseas ejecutar pruebas específicas, puedes utilizar las opciones de línea de comandos de pytest. Por ejemplo:

- **Ejecutar pruebas:**

```bash
pytest tests/test_users.py
```

- **Ver el resultado en un formato más detallado:**

```bash
pytest -v
```
