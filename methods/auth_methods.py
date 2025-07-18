import requests
from data import BASE_URL, AUTH_URL
from json import JSONDecodeError


class AuthMethods:
    def post_register_user(self, params):
        response = requests.post(
            f'{BASE_URL}{AUTH_URL}register', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        
    def post_login_user(self, params):
        response = requests.post(
            f'{BASE_URL}{AUTH_URL}login', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        
    def get_user(self,header):
        response = requests.get(
            f'{BASE_URL}{AUTH_URL}user', headers=header
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
        
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
        
    def delete_user(self, header):
        response = requests.delete(
            f'{BASE_URL}{AUTH_URL}user', headers=header
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text
    
    def post_logout_user(self, params):
        response = requests.post(
            f'{BASE_URL}{AUTH_URL}logout', json=params
        )
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response.text