import pytest
import random
import allure
from data import KNOWN_INGREDIENT_HASH
from methods.order_methods import OrderMethods
from helpers import generate_random_string


class TestOrders:
    @allure.title('Test create new order.')
    @allure.description('Test create new order with and withouth auth.')
    @pytest.mark.parametrize(
        "use_auth, order_id_present",
        [
            [True, True],
            [False, False]
        ]
    )
    def test_create_order_auth(self, register_new_user, ingredients_id_list, use_auth, order_id_present):
        order_api = OrderMethods
        _, auth_data = register_new_user

        headers = auth_data if use_auth else None
        random_ingredients = random.sample(ingredients_id_list, 3)
        create_order_payload = {
            "ingredients": random_ingredients
        }

        status_code, response = order_api().post_create_order(headers, create_order_payload)

        assert status_code == 200
        assert ('_id' in response.get('order')) == order_id_present 

    @allure.title('Test create order with various ingredients.')
    @allure.description(
        '1. Create order with valid ingredient hash.'
        '2. Create order without igredient hash.'
        '3. Create order with random ingredient hash.'
    )
    @pytest.mark.parametrize(
        "ingredient, expected_status_code",
        [
            [[KNOWN_INGREDIENT_HASH], 200],
            [[], 400],
            [generate_random_string(24), 500]
        ]
    )
    def test_create_order_ingredients(self, register_new_user, ingredient, expected_status_code):
        order_api = OrderMethods
        _, auth_data = register_new_user

        create_order_payload = {
            "ingredients": ingredient
        }

        status_code, _ = order_api().post_create_order(auth_data, create_order_payload)

        assert status_code == expected_status_code

    @allure.title('Test get user auth.')
    @allure.description('Test the get user response with and without auth.')
    @pytest.mark.parametrize(
        "use_auth, expected_status",
        [
            [True, 200],
            [False, 401]
        ]
    )
    def test_get_user_order_auth(self, login_user, use_auth, expected_status):
        order_api = OrderMethods
        auth_data = login_user

        headers = auth_data if use_auth else None

        status_code, response = order_api().get_user_orders(headers)
        print(response)

        assert status_code == expected_status