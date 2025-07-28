import requests
import allure
from data import BASE_URL
from json import JSONDecodeError


class OrderMethods:
    @allure.step('Send get ingredients request.')
    def get_ingredients(self):
        response = requests.get(
            f'{BASE_URL}ingredients'
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text

    @allure.step('Send post orders request.')    
    def post_create_order(self,header,params):
        response = requests.post(
            f'{BASE_URL}orders',
            headers=header,
            json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    @allure.step('Send get orders request.')
    def get_user_orders(self,header):
        response = requests.get(
            f'{BASE_URL}orders',
            headers=header
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        