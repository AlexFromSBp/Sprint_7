import requests
import allure

from helpers import OrderHelper
from urls import Urls

class TestOrdersListGet:

    @allure.title('Успешное получение списка заказов')
    @allure.description('Создание заказов из data, выводим список на экран. Код ответа 200, проверка тела ответа')
    def test_orders_get_list(self):

        order_data_list = OrderHelper.get_predefined_order_data()
        add_new_orders = OrderHelper.create_orders(order_data_list)

        response = requests.get(Urls.url_orders_create)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}. Response: {response.text}"

        response_json = response.json()
        assert isinstance(response_json.get('orders'), list), f"'orders' is not a list. Response: {response_json}"
