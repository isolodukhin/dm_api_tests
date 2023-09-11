from services.dm_api_account import Facade
from generic.helpers.orm_db import OrmDatabase
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_delete_v1_account_login():
    api = Facade(host='http://5.63.153.31:5051')
    login = "log_in_99"
    email = "log_in_99@dqwdq.com"
    password = "aaaaadad"
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    api.account.register_new_user(
        login=login,
        email=email,
        password=password)
    dataset = orm.get_user_by_login(login)
    for row in dataset:
        assert row.Login == login, f'User {login} not registered'
        assert row.Activated is False, f'User {login} was activated'
    orm.set_user_activated_true_by_login(login=login)
    dataset = orm.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'
    api.login.login_user(
        login=login,
        password=password)
    token = api.login.get_auth_token(login=login, password=password)
    api.login.set_headers(headers=token)
    api.login.logout_user()
    orm.delete_user_by_login(login=login)
    orm.db.close_connection()

