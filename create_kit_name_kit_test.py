import sender_stand_request
import data


#DEFINICIONES
# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo data
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201


def negative_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400

#En todas las pruebas cambié las variables kit_body refiriendo al documento data.py, con base en las observaciones. Gracias!
#PRUEBAS
# Prueba 1. El parámetro name contiene 1 caracter
def test_1_create_kit_1_character_in_name_get_success_response():
    positive_assert(data.kit_body_1) #Por ejemplo, en lugar de escribir la variable "A", aquí refiero al kit_body_1 en el archivo data.py

# Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
def test_2_create_kit_511_characters_in_name_get_success_response():
    positive_assert(data.kit_body_2)

# Prueba 3. Error. El parámetro name contiene un string vacío
def test_3_create_kit_0_characters_in_name_get_error_response():
    negative_assert(data.kit_body_3)

# Prueba 4. Error. El parámetro name contiene 512 caracteres
def test_4_create_kit_512_characters_in_name_get_error_response():
    negative_assert(data.kit_body_4)

# Prueba 5. Kit creado con éxito. El parámetro name contiene caracteres especiales
def test_5_create_kit_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_5)

# Prueba 6. Kit creado con éxito. El parámetro name contiene espacios
def test_6_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(data.kit_body_6)

# Prueba 7. Kit creado con éxito. El parámetro name contiene un string con números
def test_7_create_kit_has_number_in_first_name_get_success_response():
    positive_assert(data.kit_body_7)

# Prueba 8. Error. Falta el parámetro name en la solicitud
def test_8_create_kit_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert(kit_body)

# Prueba 9. Error. Se ha pasado un tipo de parámetro diferente en name: número
def test_9_create_kit_number_type_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = data.kit_body_9
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400