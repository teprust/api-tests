from api_client.models.register import RegisterModel
from api_client.texts.error_texts import ResponseErrorText


class TestRegisterNewUser:
    def test_auth_new_user(self, api_client):
        '''
        1. Register new user
        2. Try to auth new user from step 1
        3. Check status code is 200
        4. Check response
        '''
        # register
        body = RegisterModel().random()
        response_register = api_client.register(body=body)
        assert response_register.status_code == 200, f"Check register request, status code is {response_register.status_code}"

        # auth
        response_auth = api_client.auth(body=body)
        assert response_auth.status_code == 200, "Check auth request"
        assert response_auth.json()['token'] is not None, "Check response"

    def test_auth_new_user_2(self, api_client, register_user):
        '''
        1. Register new user
        2. Try to auth new user from step 1
        3. Check status code is 200
        4. Check response
        '''

        # auth
        response_auth = api_client.auth(body=register_user)
        assert response_auth.status_code == 200, "Check auth request"
        assert response_auth.json()['token'] is not None, "Check response"

    def test_auth_new_user_with_empty_username(self, api_client):
        '''
        1. Register new user with empty username
        2. Auth to auth user from step 1
        3. Check status code is 400
        4. Check response
        '''

        body = RegisterModel().random()
        body['login'] = None

        # auth
        response_auth = api_client.auth(body=body)
        assert response_auth.status_code == 401, "Check auth request"
        assert response_auth.json()['message'] == ResponseErrorText.BAD_REQUEST_MESSAGE
        assert response_auth.json()['status'] == ResponseErrorText.BAD_REQUEST_STATUS