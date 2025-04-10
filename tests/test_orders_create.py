import requests
import allure
import pytest
import json

from data import OrderData
from urls import Urls


class TestOrderCreate:

    @allure.title('Успешное оформление заказа при выборе цвета самоката')
    @allure.description('Оформление заказа с выбором серого, черного, обоих цветов и при пропуске выбора. Код ответа 201 Created, тело ответа содержит track номер')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_grey,
        OrderData.order_data_black,
        OrderData.order_data_black_grey,
        OrderData.order_data_no_color
    ])
    def test_order_create_color_parametrize_success(self, order_data):
        order_data_json = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}

        response = requests.post(Urls.url_orders_create, data=order_data_json, headers=headers)
        assert response.status_code == 201, f"Unexpected status code: {response.status_code}"

        response_json = response.json()
        assert 'track' in response_json, f"'track' key not found in response. Response: {response_json}"
