from requests import Response
from ..models import *
from restclient.restclient import RestClient
from dm_api_account.models.user_envelope_model import UserEnvelope


class LoginApi:

    def __init__(self, host, headers):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials, status_code: int = 201,
                              **kwargs) -> Response | UserEnvelope:
        """
        Authenticate via credentials
        :param status_code:
        :param json: login_credentials_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def delete_v1_account_login(self, **kwargs):
        """
        Logout as current user
        :return:
        """

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

        response = self.client.delete(
            path=f"/v1/account/login/all",
            **kwargs
        )
        return response
