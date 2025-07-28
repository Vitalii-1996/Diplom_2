import random
import string
import allure


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_email():
    return f'{generate_random_string(8)}@{generate_random_string(4)}.{generate_random_string(3)}'

@allure.step('generate random user payload')
def generate_random_user_payload():
    email = generate_random_email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload
