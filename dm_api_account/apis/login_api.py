from requests import Response
from ..models import *
from restclient.restclient import RestClient
from dm_api_account.models.user_envelope_model import UserEnvelope
from ..utilities import validate_request_json, validate_status_code
import allure

class LoginApi:

    def __init__(self, host, headers):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials, status_code: int = 200) -> Response:
        """
        Authenticate via credentials
        :param status_code:
        :param json: login_credentials_model
        :return:
        """

        with allure.step("Логин пользователем"):
            response = self.client.post(
                path=f"/v1/account/login",
                json=validate_request_json(json)
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            UserEnvelope(**response.json())
        return response

    def delete_v1_account_login(self, **kwargs):
        """
        Logout as current user
        :return:
        """
        with allure.step("Логаут пользователем"):
            response = self.client.delete(
                path=f"/v1/account/login",
                **kwargs
            )
            return response

    def delete_v1_account_login_all(self, **kwargs):
        """
        Logout from every device
        :return:
        """
        with allure.step("Логаут пользователем со всех устройств"):
            response = self.client.delete(
                path=f"/v1/account/login/all",
                **kwargs
            )
        return response
