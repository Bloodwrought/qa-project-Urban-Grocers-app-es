import configuration
import requests
import data
from data import kit_body

def get_kit_body():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, # Datos a enviar en la solicitud.
                         headers=data.headers)
response = get_kit_body()
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.

response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())

