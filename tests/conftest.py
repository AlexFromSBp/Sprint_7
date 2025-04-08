import requests
import pytest

from urls import Urls
from helpers import generate_random_string


@pytest.fixture
def register_new_courier():
    # Создание курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    response = requests.post(Urls.url_courier, data=payload)

    # Аутентификация для получения id
    login_payload = {
        'login': login,
        'password': password
    }
    login_response = requests.post(Urls.url_courier_login, data=login_payload)
    login_data = login_response.json()
    courier_id = login_data.get('id')

    # Логин, пароль, ник и id передать в тест
    yield response, payload, courier_id

    # Удаление карточки курьера
    delete_response = requests.delete(f"{Urls.url_courier}/{courier_id}")
