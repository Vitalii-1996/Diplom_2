import pytest
import allure
from data import EXISTING_USER, REGISTER_ERROR_MESSAGE, AUTH_ERROR_MESSAGE
from methods.auth_methods import AuthMethods
from helpers import generate_random_user_payload, generate_random_email, generate_random_string


class TestAuthUser:
    @allure.title('Test register user.')
    @allure.description(
        '1. Test success register new user.'
        '2. Test register existing user is prohibited.'
    )
    @pytest.mark.parametrize(
            'user_payload, expected_status_code',
            [
                [generate_random_user_payload(), 200],
                [EXISTING_USER, 403]
            ]
    )
    def test_register_user(self, user_payload, expected_status_code):
        auth_api = AuthMethods()
        status_code, response = auth_api.post_register_user(user_payload)
        assert status_code == expected_status_code
        assert response != None

    @allure.title('Test register user required fields.')
    @allure.description('Test register without required fields is prohibited.')
    @pytest.mark.parametrize(
            'field_name',
            ['email', 'password', 'name']
    )
    def test_register_user_required_fields(self, field_name):
        auth_api = AuthMethods()
        user_payload = generate_random_user_payload()
        del user_payload[field_name]
        status_code, response = auth_api.post_register_user(user_payload)
        assert status_code == 403
        assert response['message'] == REGISTER_ERROR_MESSAGE

    @allure.title('Test login user.')
    @allure.description(
        '1. Test success user login.'
        '2. Test login random user is prohibited.'
    )
    @pytest.mark.parametrize(
            'user_payload, expected_status_code',
            [
                [EXISTING_USER, 200],
                [generate_random_user_payload(), 401]
            ]
    )
    def test_login_user(self, user_payload, expected_status_code):
        auth_api = AuthMethods()
        del user_payload['name']
        status_code, response = auth_api.post_login_user(user_payload)
        assert status_code == expected_status_code
        assert response != None

    @allure.title('Test update user data.')
    @allure.description(
        '1. Test update name.' 
        '2. Test update email.'
        '3. Test update name and email.'
    )
    @pytest.mark.parametrize(
            'user_payload',
            [
                {'name': generate_random_string(10)},
                {'email': generate_random_email()},
                {
                    'name': generate_random_string(10),
                    'email': generate_random_email()
                }
            ]
    )
    def test_update_user(self, register_new_user, user_payload):
        auth_api = AuthMethods()
        _, auth_data = register_new_user
        status_code, response = auth_api.patch_user(auth_data, user_payload)
        assert status_code == 200
        assert response != None

    @allure.title('Test updated user without auth.')
    @allure.description('Test update user data without auth is prohibited.')
    @pytest.mark.parametrize(
            'user_payload',
            [
                {'name': generate_random_string(10)},
                {'email': generate_random_email()},
                {
                    'name': generate_random_string(10),
                    'email': generate_random_email()
                }
            ]
    )
    def test_update_user_without_auth(self, user_payload):
        auth_api = AuthMethods()
        auth_data = ''
        status_code, response = auth_api.patch_user(auth_data, user_payload)
        assert status_code == 401
        assert response.get('message') == AUTH_ERROR_MESSAGE
