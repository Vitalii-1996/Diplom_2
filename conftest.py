import pytest
from helpers import generate_random_user_payload
from methods.auth_methods import AuthMethods


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
