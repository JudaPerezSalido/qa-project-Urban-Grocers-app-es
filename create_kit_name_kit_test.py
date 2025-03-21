import sender_stand_request
import data
from sender_stand_request import post_new_kit


def get_kit_body(kit_name):
    current_body = data.kits_body.copy()
    current_body["name"] = kit_name
    return current_body

def get_new_authToken():
    user_response = sender_stand_request.post_new_user(data.user_body.copy())
    _authToken = user_response.json()["authToken"]
    new_header = data.headers.copy()
    new_header["Authorization"] = f"Bearer {_authToken}"
    return new_header


def positive_assert(name):
    kit_body = get_kit_body(name)
    post_kit = sender_stand_request.post_new_kit(kit_body, get_new_authToken())
    assert post_kit.status_code == 201
    assert post_kit.json()["name"] == name

def negative_assert(name):
    kit_body = get_kit_body(name)
    post_kit = sender_stand_request.post_new_kit(kit_body, get_new_authToken())
    assert post_kit.status_code == 400
    assert post_kit.json()["code"] == 400
    assert post_kit.json()["message"] == "No se han aprobado todos los parámetros requeridos"

def test_numero_permitido_de_caracteres_1():
    positive_assert(data.un_caracter)


def test_numero_permitido_de_caracteres_511():
    positive_assert(data.quinientos_once_caracteres)



def test_numero_de_caracteres_0():
    negative_assert(data.cero_caracteres)


def test_numero_permitido_de_caracteres_512():
    negative_assert(data.quinientos_doce_caracteres)



def test_numero_caracteres_especiales_permitidos_():
    positive_assert(data.cero_caracteres)



def test_se_permiten_espacios():
    positive_assert(data.nombre_con_espacios)


def test_se_permiten_números():
    positive_assert(data.nombre_numeros)


def test_el_parametro_no_se_pasa_en_la_solicitud():
    negative_assert(data.no_name)


def test_el_parametro_es_de_diferente_tipo():
    negative_assert(data.diferente_tipo)