from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import RegistrationModel
from dm_api_account.models.login_credentials_model import LoginCredentialsModel


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "fkweask444fewf44"
    password = "aaaafadad"
    email = "qwdwsqdd11s235@dqwdq.com"
    json = RegistrationModel(
        login=login,
        email=email,
        password=password
    )
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть равен 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    json = LoginCredentialsModel(
        login=login,
        password=password,
        rememberMe=False
    )
    response = api.login.post_v1_account_login(json=json)
    assert response.status_code == 200, f'Статус код ответа должен быть равен 201, но он равен {response.status_code}'
