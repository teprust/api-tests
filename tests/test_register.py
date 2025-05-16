import requests
from faker import Faker

URL = "http://158.160.87.146:5000"
fake = Faker()

class TestRegisterNewUser:
    def test_register_new_user(self):
        '''
        1. Try to register new user
        2. Check status code is 200
        3. Check response
        '''
        body = {"login": fake.email(), "password": "aaaa"}
        response = requests.post(url=f"{URL}/api/register", json=body)
        assert response.status_code == 200, f"Check register request, status code is {response.status_code}"

        # В ответ получаем что-то в поле
        assert response.json()['status'] is not None

        # Проверяем тип поля в ответе
        assert isinstance(response.json()['status'], str)

        # Проверяем текст поля ответа
        assert response.json()['status'] == "Successful"

    def test_register_new_user_with_empty_username(self):
        '''
        1. Try to register new user with empty username
        2. Check status code is 400
        3. Check response
        '''
        body = {"login": None, "password": "aaaa"}
        response = requests.post(url=f"{URL}/api/register", json=body)
        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"

        # В ответ получаем что-то в поле
        assert response.json()['status'] is not None

        # Проверяем тип поля в ответе
        assert isinstance(response.json()['status'], str)

        # Проверяем текст поля ответа
        assert response.json()['status'] == "Error"

    def test_register_new_user_with_empty_password(self):
        '''
        1. Try to register new user with empty password
        2. Check status code is 400
        3. Check response
        '''
        body = {"login": fake.email(), "password": None}
        response = requests.post(url=f"{URL}/api/register", json=body)
        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"

        # В ответ получаем что-то в поле
        assert response.json()['status'] is not None

        # Проверяем тип поля в ответе
        assert isinstance(response.json()['status'], str)

        # Проверяем текст поля ответа
        assert response.json()['status'] == "Error"