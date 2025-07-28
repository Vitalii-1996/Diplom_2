import requests
import allure
from data import BASE_URL, AUTH_URL
from json import JSONDecodeError


class AuthMethods:
    @allure.step('Send post register request.')
    def post_register_user(self, params):
        response = requests.post(
            f'{BASE_URL}{AUTH_URL}register', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    @allure.step('Send post login request.')
    def post_login_user(self, params):
        response = requests.post(
            f'{BASE_URL}{AUTH_URL}login', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    @allure.step('Send get user request.')
    def get_user(self,header):
        response = requests.get(
            f'{BASE_URL}{AUTH_URL}user', headers=header
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    @allure.step('Send patch user request.')
    def patch_user(self,header,params):
        response = requests.patch(
            f'{BASE_URL}{AUTH_URL}user',
            headers=header,
            json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    @allure.step('Send delete user request.')
    def delete_user(self, header):
        response = requests.delete(
            f'{BASE_URL}{AUTH_URL}user', headers=header
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    @allure.step('Send post logout request.')
    def post_logout_user(self, params):
        response = requests.post(
            f'{BASE_URL}{AUTH_URL}logout', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text