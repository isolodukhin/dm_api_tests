from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.login_credentials_model import LoginCredentials
from dm_api_account.models.user_envelope_model import UserRole, Rating
from hamcrest import *

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "fsk447fewf44"
    password = "aaaafadad"
    email = "q58@dqwdq.com"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    json = LoginCredentials(
        login=login,
        password=password,
        rememberMe=False
    )
    response = api.login.post_v1_account_login(json=json)
    assert_that(response.resource, has_properties(
        {
            "login": "fkw30",
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())

