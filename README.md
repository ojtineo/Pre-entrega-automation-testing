# Proyecto de Pruebas Automatizadas con Python y Selenium WebDriver

## 1. Propósito del proyecto

El objetivo de este proyecto es automatizar pruebas funcionales sobre el sitio web de demostración [SauceDemo](https://www.saucedemo.com/), utilizando Python, Selenium WebDriver y Pytest.

Las pruebas permiten verificar el funcionamiento del inicio de sesión, la visualización del inventario de productos y las operaciones básicas del carrito de compras.

## 2. Tecnologías utilizadas

* Python: lenguaje de programación utilizado para desarrollar las pruebas.
* Selenium WebDriver: herramienta para automatizar la interacción con el navegador.
* Pytest: framework para ejecutar y organizar las pruebas automatizadas.
* pytest-html: plugin para generar reportes HTML con los resultados de la ejecución.
* Google Chrome: navegador utilizado para ejecutar las pruebas.

## 3. Alcance de las pruebas

### Login

* Verificar el inicio de sesión exitoso con credenciales válidas.
* Comprobar la navegación hacia la página de inventario.
* Validar la presencia del logo y el título de productos.
* Verificar el rechazo de credenciales incorrectas y la visualización del mensaje de error.

### Inventario

* Validar el título de la página.
* Comprobar que se muestren productos.
* Verificar el nombre y el precio del primer producto.
* Comprobar la visibilidad del menú y del selector de ordenamiento.

### Carrito de compras

* Iniciar sesión y acceder al inventario.
* Agregar un producto al carrito.
* Verificar que el contador del carrito muestre una unidad.
* Comprobar que el producto agregado aparezca en el carrito.

## 4. Requisitos previos

Antes de ejecutar el proyecto, se necesita:

* Tener Python instalado.
* Tener Google Chrome instalado.
* Tener acceso a Internet.
* Instalar las dependencias necesarias del proyecto.

## 5. Instalación de dependencias

Clonar el repositorio y acceder a la carpeta del proyecto:

git clone URL_DEL_REPOSITORIO
cd NOMBRE_DEL_REPOSITORIO

Instalar las dependencias:

python -m pip install pytest selenium pytest-html


Selenium Manager puede encargarse de resolver el controlador del navegador cuando la instalación y el entorno lo permiten.

## 6. Ejecución de las pruebas

La configuración de Pytest se encuentra en `pytest.ini` y establece los siguientes parámetros:

[pytest]
python_files = test_*.py
python_functions = test_*
addopts = -v -s --html=report/reporte.html --self-contained-html

Para ejecutar las pruebas, utilizar:

pytest

El comando ejecuta los tests detectados por Pytest y utiliza la configuración definida en `pytest.ini`.

El reporte HTML se configura en la siguiente ruta:

report/reporte.html


La carpeta `report` debe existir antes de la ejecución para que Pytest pueda guardar el archivo.

## 7. Reporte de resultados

Al finalizar la ejecución, Pytest genera un reporte HTML con los resultados de las pruebas, siempre que la ejecución y la escritura del archivo se completen correctamente.

El reporte permite consultar los resultados de la ejecución de los casos de prueba.

## 8. Evidencias de ejecución

El proyecto contempla como evidencia:

* Reporte HTML: resultados de la ejecución de las pruebas automatizadas.

## 9. Autor

Proyecto de práctica de QA Automation desarrollado con Python, Selenium WebDriver y Pytest.
