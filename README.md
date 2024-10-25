# qa-project-Urban-Grocers-app-es
Proyecto Sprint 7

# Pasos a seguir para ejecutar las pruebas
1. Abrir este proyecto (qa-project-Urban-Grocers-app-es) en PyCharm.
2. En el botón Python Packages, asegurarse que los paquetes requests y pytest estén descargados y actualizados.
3. De no estar instalados/actualizados, descargar/actualizar ambos paquetes.
4. Seleccionar el archivo configuration.py
5. En el campo URL_SERVICE cambiar la URL existente por la de un servidor nuevo.
6. Seleccionar el archivo create_kit_name_kit_test.py
7. En la barra superior, asegurarse que la lista desplegable al lado del botón de "Play" diga "Current file".
8. Hacer click en el botón de "Play" o ejecutando el comando "python -m pytest" en la terminal de Pycharm.

# Lista de comprobación detallando las pruebas automatizadas realizadas al correr el archivo create_name_kit_test

Lista de comprobación de pruebas
№	Description:
Prueba 1	El número permitido de caracteres (1): kit_body = { "name": "a"}	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
Prueba 2	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}	Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
Prueba 3	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	Código de respuesta: 400
Prueba 4	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	Código de respuesta: 400
Prueba 5	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
Prueba 6	Se permiten espacios: kit_body = { "name": " A Aaa " }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
Prueba 7	Se permiten números: kit_body = { "name": "123" }	Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
Prueba 8	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400
Prueba 9	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	Código de respuesta: 400