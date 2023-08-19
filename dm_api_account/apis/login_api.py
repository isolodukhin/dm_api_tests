from requests import Response
from ..models import login_credentials_model
from requests import session


class LoginApi:

    def __init__(self, host, headers):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers = headers

    def post_v1_account_login(self, json: login_credentials_model, **kwargs) -> Response:
        """
        Authenticate via credentials
        :param json: login_credentials_model
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json,
            **kwargs
        )
        return response

    def delete_v1_account_login(self, **kwargs):
        """
        Logout as current user
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            **kwargs
        )
        return response

    def delete_v1_account_login_all(self, **kwargs):
        """
        Logout from every device
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
            **kwargs
        )
        return response