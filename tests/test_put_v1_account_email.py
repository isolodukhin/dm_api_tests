import time
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.change_email_model import ChangeEmail
from dm_api_account.models.user_envelope_model import UserRole, Rating
from hamcrest import *

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    login = "fkw76fewf4982"
    password = "aaaaadad"
    email = "qwdws7992@dqwdq.com"
    new_email = '1s73851@dqwdq.com'
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    response = api.account.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    json = ChangeEmail(
        login=login,
        email=new_email,
        password=password
    )
    response = api.account.put_v1_account_email(json=json)
    assert_that(response.resource, has_properties(
        {
            "login": "fkw30",
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())

