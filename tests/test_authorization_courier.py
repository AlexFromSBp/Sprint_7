import requests
import allure
import pytest

from urls import Urls
from helpers import generate_random_string


class TestCourierLogin:

    @allure.title('Успешная аутентификация курьера при вводе корректного логина и пароля')
    @allure.description('Генерация карточки курьера, аутентификация. Код ответа 200 OK, id: [.....]')
    def test_courier_login_success(self, register_new_courier):
        with allure.step("Получить данные зарегистрированного курьера"):
            response, payload, courier_id = register_new_courier
            login = payload['login']
            password = payload['password']

        with allure.step("Сформировать payload для авторизации"):
            auth_payload = {
                'login': login,
                'password': password
            }

        with allure.step("Отправить запрос на авторизацию курьера"):
            response = requests.post(Urls.url_courier_login, data=auth_payload)
            allure.attach(f"Request payload: {auth_payload}", name="Request Data")
            allure.attach(f"Response: {response.text}", name="Response Data")

        with allure.step("Проверить статус код ответа"):
            assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

        with allure.step("Проверить наличие ID курьера в ответе"):
            response_json = response.json()
            assert 'id' in response_json, "Response does not contain 'id'"

    @allure.title('Проверка ошибок аутентификации при неполных данных')
    @allure.description('Тестирование случаев пропуска обязательных полей')
    @pytest.mark.parametrize("login, password, message", [
        ("", "valid_password", "Недостаточно данных для входа"),
        ("valid_login", "", "Недостаточно данных для входа"),
        ("", "", "Недостаточно данных для входа")
    ])

    def test_courier_login_missing_fields(self, register_new_courier, login, password, message):
        with allure.step("Получить данные зарегистрированного курьера"):
            response, registered_payload, courier_id = register_new_courier

        with allure.step("Подготовить тестовые данные"):
            if password == "valid_password":
                password = registered_payload['password']
            if login == "valid_login":
                login = registered_payload['login']

            payload = {
                'login': login,
                'password': password
            }
            allure.attach(f"Test data - login: '{login}', password: '{password}'", name="Test Parameters")

        with allure.step("Отправить запрос с неполными данными"):
            response = requests.post(Urls.url_courier_login, data=payload)
            allure.attach(f"Response: {response.text}", name="Response Data")

        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400, f"Unexpected status code: {response.status_code}"

        with allure.step("Проверить сообщение об ошибке"):
            response_json = response.json()
            assert response_json == {'message': message}, f"Unexpected response: {response_json}"

    @allure.title('Проверка ошибок аутентификации при вводе некорректных данных')
    @allure.description('Генерация карточки курьера, попытка аутентификации с некорректным логином, паролем. Код ответа 404 Not Found')
    @pytest.mark.parametrize("login, password, message", [
        ("nonexistent_login", "valid_password", "Учетная запись не найдена"),
        ("valid_login", "wrong_password", "Учетная запись не найдена"),
        ("invalid_login", "invalid_password", "Учетная запись не найдена")
    ])

    def test_courier_login_invalid_credentials(self, register_new_courier, login, password, message):
        with allure.step("Получить данные зарегистрированного курьера"):
            response, registered_payload, courier_id = register_new_courier

        with allure.step("Подготовить тестовые данные"):
            if password == "valid_password":
                password = registered_payload['password']
            if login == "valid_login":
                login = registered_payload['login']
            if login == "nonexistent_login":
                login = generate_random_string(10)
            if password == "wrong_password":
                password = generate_random_string(10)

            payload = {
                'login': login,
                'password': password
            }
            allure.attach(f"Test data - login: '{login}', password: '{password}'", name="Test Parameters")

        with allure.step("Отправить запрос с некорректными данными"):
            response = requests.post(Urls.url_courier_login, data=payload)
            allure.attach(f"Response: {response.text}", name="Response Data")

        with allure.step("Проверить статус код 404"):
            assert response.status_code == 404, f"Unexpected status code: {response.status_code}"

        with allure.step("Проверить сообщение об ошибке"):
            response_json = response.json()
            assert response_json == {'message': message}, f"Unexpected response: {response_json}"
