# Automatización de compra

Este proyecto automatiza una compra de prueba en [SauceDemo](https://www.saucedemo.com) con Selenium y Python.

## Escenario

El script `login.py` realiza estos pasos:

1. Abre SauceDemo e inicia sesión.
2. Agrega **Sauce Labs Backpack** al carrito.
3. Abre el carrito.
4. Verifica que el producto aparezca en la página.

Si la validación se completa, muestra `Prueba aprobada.`. Si falla, Python genera un error de aserción.

## Requisitos

- Python 3
- Google Chrome
- Selenium para Python

Instala Selenium desde una terminal:

```bash
python -m pip install selenium
```

Selenium Manager normalmente detecta y administra el controlador de Chrome automáticamente.

## Ejecución

Desde la carpeta `AutomatizacionQA`, ejecuta:

```bash
python login.py
```

El navegador se abrirá de forma visible. El script incluye pausas para permitir observar cada etapa y cierra el navegador al terminar.

## Credenciales de demostración

El script usa las credenciales de prueba públicas de SauceDemo:

- Usuario: `standard_user`
- Contraseña: `secret_sauce`
