# Automatización de pruebas web con Selenium y Pytest

## Descripción del proyecto

Proyecto de automatización de pruebas funcionales sobre el sitio web [SauceDemo](https://www.saucedemo.com/), desarrollado con Python, Selenium WebDriver y Pytest.

El objetivo es validar funcionalidades principales de la aplicación mediante pruebas automatizadas y generar un informe HTML con los resultados de la ejecución.

## Tecnologías utilizadas

* Python: lenguaje de programación.
* Selenium WebDriver: automatización de la interacción con el navegador.
* Pytest: ejecución y organización de las pruebas.
* pytest-html: generación del informe HTML.
* Google Chrome:* navegador utilizado para ejecutar las pruebas.

## Pruebas implementadas

### Inicio de sesión

* Validación del inicio de sesión exitoso.
* Comprobación de la URL de inventario.
* Verificación del logo y del título de productos.
* Validación del mensaje de error ante credenciales incorrectas.

### Inventario

* Verificación del título de la página.
* Comprobación de que existan productos.
* Validación del nombre y precio del primer producto.
* Verificación de la visibilidad del menú y del selector de ordenamiento.

### Carrito de compras

* Incorporación de un producto al carrito.
* Comprobación de la cantidad de productos agregados.
* Verificación de que el producto agregado aparezca en el carrito.

## Requisitos previos

* Python instalado.
* Google Chrome instalado.
* Conexión a Internet.
* Dependencias del proyecto instaladas.

## Instalación

Instalar las dependencias necesarias desde la terminal:

python -m pip install pytest selenium pytest-html

## Ejecución de las pruebas

Desde la carpeta raíz del proyecto, ejecutar en la terminal:

pytest

La configuración de `pytest.ini` establece la ejecución detallada de las pruebas y la generación de un informe HTML.

## Informe de resultados

El informe se genera en:

`report/reporte.html`

Para consultarlo, abrir ese archivo con un navegador web después de ejecutar las pruebas.

La carpeta `report` debe existir antes de la ejecución para que Pytest pueda guardar el informe en esa ubicación.

## Estado de las funcionalidades

* Pruebas automatizadas de login, inventario y carrito: implementadas en los scripts compartidos.
* Generación de informe HTML: configurada mediante `pytest-html`.


## Repositorio

El proyecto se publicará en GitHub cuando se complete la preparación del repositorio.
