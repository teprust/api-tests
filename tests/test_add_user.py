from api_client.models.add_user import AddUserModel
from api_client.models.register import RegisterModel
from api_client.texts.response_texts import ResponseTest


class TestAddUser:
    def test_add_new_user(self, api_client):
        '''
        1. Register new user
        2. Auth user from step 1
        3. Try to add new user
        4. Check status code is 200
        5. Check response
        '''
        # register
        body = RegisterModel().random()
        response_register = api_client.register(body=body)
        assert response_register.status_code == 200, f"Check register request, status code is {response_register.status_code}"

        # auth
        response_auth = api_client.auth(body=body)
        assert response_auth.status_code == 200, "Check auth request"
        assert response_auth.json()['token'] is not None, "Check response"

        # add new user
        token = response_auth.json()['token']
        header = {"Authorization": f"Bearer {token}"}
        body_user = AddUserModel().random()
        response_add = api_client.add_user(body=body_user, header=header)
        assert response_add.status_code == 200
        assert response_add.json()['status'] == ResponseTest.CREATE_USER_STATUS

    def test_add_new_user_2(self, api_client, auth_user):
        '''
        1. Register new user
        2. Auth user from step 1
        3. Try to add new user
        4. Check status code is 200
        5. Check response
        '''

        header = auth_user
        body_user = AddUserModel().random()
        response_add = api_client.add_user(body=body_user, header=header)
        assert response_add.status_code == 200
        assert response_add.json()['status'] == ResponseTest.CREATE_USER_STATUS