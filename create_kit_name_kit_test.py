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

    assert kit_response.json() != ""

    # Comprobar que el resultado de la solicitud se guarda en kit_body_response
    kit_body_response = sender_stand_request.get_kit_body()

    # String que debe estar en el cuerpo de respuesta
    str_user = kit_body["name"]

    # Comprueba si el kit existe y es único
    assert kit_body_response.text.count(str_user) == 1


def negative_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"


#PRUEBAS
# Prueba 1. El parámetro name contiene 1 caracter
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert("A")

# Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
def test_create_kit_511_characters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3. Error. El parámetro name contiene un string vacío
def test_create_kit_0_characters_in_name_get_error_response():
    negative_assert("")

# Prueba 4. Error. El parámetro name contiene 512 caracteres
def test_create_kit_512_characters_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 5. Kit creado con éxito. El parámetro name contiene caracteres especiales
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Prueba 6. Kit creado con éxito. El parámetro name contiene espacios
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert("A Aaa")

# Prueba 7. Error. El parámetro name contiene un string con números
def test_create_user_has_number_in_first_name_get_error_response():
    positive_assert("123")

# Prueba 8. Error. Falta el parámetro name en la solicitud
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    kit_body = data.kit_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert(kit_body)

# Prueba 9. Error. El parámetro contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body("")
    # Comprueba la respuesta
    negative_assert(kit_body)

# Prueba 10. Error. El tipo del parámetro name: número
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(12)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400