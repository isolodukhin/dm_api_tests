import json
import time

from requests import Response
from restclient.restclient import RestClient
import allure


def decorator(fn):
    def wrapper(*args, **kwargs):
        for i in range(5):
            response = fn(*args, **kwargs)
            emails = response.json()['items']
            if len(emails) < 5:
                print(f'attempt{i}')
                continue
            else:
                return response

    return wrapper


class MailhogApi:

    def __init__(self, host='http://5.63.153.31:5025'):
        self.host = host
        self.client = RestClient(host=host)

    @decorator
    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        with allure.step(f"Получить {limit} писем"):
            response = self.client.get(
                path=f"/api/v2/messages",
                params={
                    'limit': limit
                }
            )

        return response

    def get_token_from_last_email(self) -> str:
        """
        Get user activation token from last email
        :return:
        """
        with allure.step("Получить токен активации из последнего email"):
            emails = self.get_api_v2_messages(1).json()
            token_url = json.loads(emails['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
            token = token_url.split('/')[-1]
        return token

    def get_token_by_login(self, login: str, attempt=50):
        with allure.step("Получить токен по логину"):
            if attempt == 0:
                raise AssertionError(f'Не удалось получить письмо с логином {login}')
            emails = decorator(self.get_api_v2_messages)(100).json()['items']
            for email in emails:
                user_data = json.loads(email['Content']['Body'])
                if login == user_data.get('Login'):
                    token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                    print(token)
                    return token
            time.sleep(2)
            return self.get_token_by_login(login=login, attempt=attempt - 1)

    def get_reset_password_token_by_login(self, login: str, attempt=50):
        with allure.step("Получить токен сбрасывания пароля по логину"):
            if attempt == 0:
                raise AssertionError(f'Не удалось получить письмо с логином {login}')
            emails = decorator(self.get_api_v2_messages)(100).json()['items']
            for email in emails:
                user_data = json.loads(email['Content']['Body'])
                if login == user_data.get('Login'):
                    token = user_data['ConfirmationLinkUri'].split('/')[-1]
                    print(token)
                    return token
        time.sleep(2)
        return self.get_token_by_login(login=login, attempt=attempt - 1)

    def delete_all_messages(self):
        with allure.step("Удалить все сообщения"):
            response = self.client.delete(path='/api/v1/messages')
        return response
