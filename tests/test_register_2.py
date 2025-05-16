from api_client.models.register import RegisterModel


class TestRegisterNewUser:
    def test_register_new_user_2(self, api_client):
        '''
        1. Try to register new user
        2. Check status code is 200
        3. Check response
        '''
        body = RegisterModel().random()
        response = api_client.register(body=body)
        assert response.status_code == 200, f"Check register request, status code is {response.status_code}"

        # В ответ получаем что-то в поле
        assert response.json()['status'] is not None

        # Проверяем тип поля в ответе
        assert isinstance(response.json()['status'], str)

        # Проверяем текст поля ответа
        assert response.json()['status'] == "Successful"

    def test_register_new_user_with_empty_username_2(self, api_client):
        '''
        1. Try to register new user with empty username
        2. Check status code is 400
        3. Check response
        '''
        body = RegisterModel().random()
        body['login'] = None
        response = api_client.register(body=body)

        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"

        # В ответ получаем что-то в поле
        assert response.json()['status'] is not None
        assert response.json()['message'] is not None

        # Проверяем тип поля в ответе
        assert isinstance(response.json()['status'], str)
        assert isinstance(response.json()['message'], str)

        # Проверяем текст поля ответа
        assert response.json()['status'] == "Error"
        assert response.json()['message'] == "Missing login or password"

    def test_register_new_user_with_empty_password_2(self, api_client):
        '''
        1. Try to register new user with empty password
        2. Check status code is 400
        3. Check response
        '''
        body = RegisterModel().random()
        body['password'] = None
        response = api_client.register(body=body)

        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"

        # В ответ получаем что-то в поле
        assert response.json()['status'] is not None
        assert response.json()['message'] is not None

        # Проверяем тип поля в ответе
        assert isinstance(response.json()['status'], str)
        assert isinstance(response.json()['message'], str)

        # Проверяем текст поля ответа
        assert response.json()['status'] == "Error"
        assert response.json()['message'] == "Missing login or password"