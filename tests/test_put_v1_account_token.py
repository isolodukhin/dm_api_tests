import time

from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
from hamcrest import *
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "fkw33"
    password = "aaaafadad"
    email = "qwd33@dqwdq.com"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    response = api.account.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token, status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "fkw30",
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())
