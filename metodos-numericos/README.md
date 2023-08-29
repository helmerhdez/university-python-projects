# : Métodos Numéricos

## Requisitos Previos

Antes de comenzar con este proyecto, asegúrate de tener lo siguiente instalado en tu sistema:

- **Python y pip:** Asegúrate de que tanto Python como pip estén configurados en tus variables de entorno para que puedas acceder a ellos desde cualquier ubicación en tu sistema. Puedes verificarlo ejecutando los siguientes comandos:

    ```sh
    python --version
    pip --version
    ```

    Si recibes errores o los comandos no son reconocidos, es posible que necesites configurar las variables de entorno correctamente.


## Configuración Inicial

1. **Clona el Repositorio:** Comienza clonando este repositorio en tu máquina local usando el siguiente comando:

    ```sh
    git clone https://github.com/helmerhdez/university-python-projects.git
    
    cd university-python-projects

    cd metodos-numericos
    ```

2. **Crea un Entorno Virtual:** Crea y activa un entorno virtual para aislar las dependencias del proyecto:

    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instala Dependencias:** Instala las dependencias del proyecto desde el archivo `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

4. **Configura la Aplicación:** Asegúrate de configurar la aplicación según tus necesidades en el archivo `app/__init__.py`, incluyendo las configuraciones y extensiones que puedas necesitar.

## Ejecución

1. **Ejecuta la Aplicación:** Inicia el servidor de desarrollo ejecutando el archivo `run.py`:

    ```sh
    python run.py
    ```

2. **Accede a la Aplicación:** Abre tu navegador y ve a [http://127.0.0.1:5000/](http://127.0.0.1:5000/) para acceder a la página de inicio de la aplicación.

## Detener la Aplicación

Para detener la aplicación, regresa a la terminal donde se está ejecutando y presiona `Ctrl + C`. No olvides desactivar el entorno virtual cuando hayas terminado:

```sh
deactivate
