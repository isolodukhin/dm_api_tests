from services.dm_api_account import Facade
import structlog
from dm_api_account.models.user_envelope_model import UserRole
from hamcrest import *

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = Facade(host='http://5.63.153.31:5051')
    login = "log_in_12"
    email = "log_in_12@dqwdq.com"
    password = "aaaaadad"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password)
    api.account.activate_registered_user(login=login)
    response = api.login.login_user(
        login=login,
        password=password)
    assert_that(response.resource, has_properties(
        {
            "login": "log_in_12",
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())

