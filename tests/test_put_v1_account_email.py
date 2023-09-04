from services.dm_api_account import Facade
import structlog
from dm_api_account.models.user_envelope_model import UserRole
from hamcrest import *

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_email():
    api = Facade(host='http://5.63.153.31:5051')
    login = "fkw76fewf498211"
    password = "aaaaadad"
    email = "qwdws799211@dqwdq.com"
    new_email = '1s7385111@dqwdq.com'
    api.account.register_new_user(
        login=login,
        email=email,
        password=password)
    api.account.activate_registered_user(login=login)
    response = api.account.change_user_email(
        login=login,
        password=password,
        email=new_email
    )
    assert_that(response.resource, has_properties(
        {
            "login": "fkw76fewf498211",
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())

