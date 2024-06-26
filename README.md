# Proyecto de Automatización con Python y Selenium

Este proyecto es una suite de pruebas automatizadas utilizando Python y Selenium. A continuación se describen los pasos para configurar el entorno y ejecutar las pruebas.

## Requisitos Previos

- Python 3.8 o superior: [Descargar Python](https://www.python.org/downloads/)
- Google Chrome: [Descargar Chrome](https://www.google.com/chrome/)
- ChromeDriver: [Descargar ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Instalación

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local usando `git`:

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

### 2. Crear un Entorno Virtual

Crea un entorno virtual para instalar las dependencias del proyecto:
python -m venv venv

Activa el entorno virtual:
.\venv\Scripts\activate

### 3. Instalar Dependencias

pip install -r requirements.txt

### 4. Configurar ChromeDriver

Descarga la versión adecuada de ChromeDriver para tu sistema operativo desde aquí y coloca el ejecutable en una ubicación de tu sistema que esté en el PATH, o especifica la ruta al ChromeDriver en tu script de prueba.
Por ejemplo, si descargaste chromedriver.exe y lo colocaste en D:\WebDrivers\chromedriver-win64\chromedriver.exe, asegúrate de que tu script lo use correctamente

### 5. Ejecutar las Pruebas

Para ejecutar las pruebas, asegúrate de que tu entorno virtual esté activado y ejecuta tu script de prueba:

python nombre_de_tu_script.py
