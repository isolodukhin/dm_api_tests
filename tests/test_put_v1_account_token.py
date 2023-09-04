from services.dm_api_account import Facade
import structlog
from hamcrest import *
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host='http://5.63.153.31:5051')
    login = "fkw333"
    password = "aaaafadad"
    email = "qwd331@dqwdq.com"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password)
    response = api.account.activate_registered_user(login=login)
    assert_that(response.resource, has_properties(
        {
            "login": "fkw333",
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())
