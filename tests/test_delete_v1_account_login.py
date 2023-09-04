from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_delete_v1_account_login():
    api = Facade(host='http://5.63.153.31:5051')
    login = "log_in_7"
    email = "log_in_7@dqwdq.com"
    password = "aaaaadad"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password)
    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password)
    token = api.login.get_auth_token(login='log_in_7', password='aaaaadad')
    api.login.set_headers(headers=token)
    api.login.logout_user()

