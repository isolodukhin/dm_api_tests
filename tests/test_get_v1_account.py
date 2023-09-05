from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "log_in_34"
    email = "log_in_34@dqwdq.com"
    password = "aaaaadad"

    api.account.register_new_user(
        login=login,
        email=email,
        password=password)
    api.account.activate_registered_user(login=login)
    response = api.login.login_user(
        login=login,
        password=password)
    token = api.login.get_auth_token(login='log_in_34', password='aaaaadad')
    api.account.set_headers(headers=token)
    api.login.set_headers(headers=token)
    api.account.get_current_user_info()

