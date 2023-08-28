from requests import Response
from ..models.registration_model import RegistrationModel
from ..models.reset_password_model import ResetPasswordModel
from ..models.change_email_model import ChangeEmailModel
from ..models.change_password_model import ChangePasswordModel
from restclient.restclient import RestClient
from dm_api_account.models.user_envelope_model import UserEnvelopeModel



class AccountApi:

    def __init__(self, host, headers):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        Register new user
        :param json: registration_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: ResetPasswordModel, **kwargs) -> Response:
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePasswordModel, **kwargs) -> Response:
        """
        Change registered user password
        :param json: change_password_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        Activate registered user
        :param token
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",
            **kwargs)
        return response