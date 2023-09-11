from services.dm_api_account import Facade
import structlog
from dm_api_account.models.reset_password_model import ResetPassword

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = Facade(host='http://5.63.153.31:5051')
    login = "log_in_80"
    email = "log_in_80@dqwdq.com"
    password = "aaaaadad"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password)
    api.account.activate_registered_user(login=login)
    api.account.reset_user_password(
        login=login,
        email=email
    )


