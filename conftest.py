import pytest
from helpers import generate_random_user_payload
from methods.auth_methods import AuthMethods
from methods.order_methods import OrderMethods
from data import EXISTING_USER, LOGOUT_MESSAGE


@pytest.fixture
def register_new_user():
    user_payload = generate_random_user_payload()
    auth_api = AuthMethods()

    _, response = auth_api.post_register_user(user_payload)
    auth_token = response.get('accessToken')
    auth_data = {"Authorization" : auth_token}
    
    yield user_payload, auth_data

    status_code, _ = auth_api.delete_user(auth_data)
    assert status_code == 202

@pytest.fixture
def ingredients_id_list():
    order_api = OrderMethods()
    _, response = order_api.get_ingredients()
    ingredients = list()
    for ingredient in response.get('data'):
        ingredients.append(ingredient.get('_id'))
    return ingredients

@pytest.fixture
def login_user():
    user_payload = EXISTING_USER
    auth_api = AuthMethods()

    _, response = auth_api.post_login_user(user_payload)
    auth_token = response.get('accessToken')
    refresh_token = response.get('refreshToken')
    auth_data = {"Authorization" : auth_token}
    
    yield auth_data

    refresh_data = {"token": refresh_token}
    status_code, response = auth_api.post_logout_user(refresh_data)
    assert status_code == 200
    assert response.get('message') == LOGOUT_MESSAGE