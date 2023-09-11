from services.dm_api_account import Facade
import structlog
from generic.helpers.orm_db import OrmDatabase

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = Facade(host='http://5.63.153.31:5051')
    login = "log_in_102"
    email = "log_in_102@dqwdq.com"
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
    api.account.reset_user_password(
        login=login,
        email=email
    )
    orm.delete_user_by_login(login=login)
    orm.db.close_connection()


