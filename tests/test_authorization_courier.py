import requests
import allure

from urls import Urls
from helpers import generate_random_string


class TestCourierLogin:

    @allure.title('Успешная аутентификация курьера при вводе корректного логина и пароля')
    @allure.description('Генерация карточки курьера, аутентификация. Код ответа 200 OK, id: [.....]')
    def test_courier_login_success(self, register_new_courier):
        response, payload, courier_id = register_new_courier
        login = payload['login']
        password = payload['password']

        payload = {
            'login': login,
            'password': password
        }

        response = requests.post(Urls.url_courier_login, data=payload)
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        response_json = response.json()
        assert 'id' in response_json, "Response does not contain 'id'"

    @allure.title('Возникновение ошибки при пропуске поля логин для аутентификации')
    @allure.description('Генерация карточки курьера, попытка аутентификации без заполнения поля логин. Код ответа 400 Bad Request, тело ответа Недостаточно данных для входа')
    def test_courier_login_empty_login(self, register_new_courier):
        response, payload, courier_id = register_new_courier
        login = ''
        password = payload['password']

        payload = {
            'login': login,
            'password': password
        }
        response = requests.post(Urls.url_courier_login, data=payload)
        assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
        assert response.json() == {
            'message': 'Недостаточно данных для входа'}, f"Unexpected response: {response.json()}"


    @allure.title('Возникновение ошибки при пропуске поля пароль для аутентификации')
    @allure.description('Генерация карточки курьера, попытка аутентификации без заполнения поля пароль. Код ответа 400 Bad Request, тело ответа Недостаточно данных для входа')
    def test_courier_login_empty_password(self, register_new_courier):
        response, payload, courier_id = register_new_courier
        login = payload['login']
        password = ''

        payload = {
            'login': login,
            'password': password
        }
        response = requests.post(Urls.url_courier_login, data=payload)
        assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
        assert response.json() == {'message': 'Недостаточно данных для входа'}, f"Unexpected response: {response.json()}"

    @allure.title('Возникновение ошибки аутентификации курьера при вводе некорректного логина')
    @allure.description('Генерация карточки курьера, попытка аутентификации с некорректным логином. Код ответа 404 Not Found, тело ответа Учетная запись не найдена')
    def test_courier_login_wrong_login(self, register_new_courier):
        response, payload, courier_id = register_new_courier
        login = generate_random_string(10)
        password = payload['password']

        payload = {
            'login': login,
            'password': password
        }
        response = requests.post(Urls.url_courier_login, data=payload)
        assert response.status_code == 404, f"Unexpected status code: {response.status_code}"
        assert response.json() == {'message': 'Учетная запись не найдена'}, f"Unexpected response: {response.json()}"

    @allure.title('Возникновение ошибки аутентификации курьера при вводе некорректного пароля')
    @allure.description('Генерация карточки курьера, попытка аутентификации с некорректным паролем. Код ответа 404 Not Found, тело ответа Учетная запись не найдена.')
    def test_courier_login_wrong_password(self, register_new_courier):
        response, payload, courier_id = register_new_courier
        login = payload['login']
        password = generate_random_string(10)

        payload = {
            'login': login,
            'password': password
        }
        response = requests.post(Urls.url_courier_login, data=payload)
        assert response.status_code == 404, f"Unexpected status code: {response.status_code}"
        assert response.json() == {'message': 'Учетная запись не найдена'}, f"Unexpected response: {response.json()}"
