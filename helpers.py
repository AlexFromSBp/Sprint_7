import requests
import random
import string
import json
from data import OrderData
from urls import Urls

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

class OrderHelper:
    @staticmethod
    def create_orders(order_data_list):
        order_data_json = json.dumps(order_data_list)
        response = requests.post(Urls.url_orders_create, data=order_data_json)
        return response

    @staticmethod
    def get_predefined_order_data():
        return [
            OrderData.order_data_grey,
            OrderData.order_data_black,
            OrderData.order_data_black_grey,
            OrderData.order_data_no_color
        ]