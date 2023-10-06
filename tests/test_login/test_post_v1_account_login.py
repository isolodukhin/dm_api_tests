
from apis.dm_api_account.models.user_envelope_model import UserRole
from hamcrest import *


def test_post_v1_account_login(dm_api_facade,orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password)
    dataset = orm_db.get_user_by_login(login)
    for row in dataset:
        assert row.Login == login, f'User {login} not registered'
        assert row.Activated is False, f'User {login} was activated'
    orm_db.set_user_activated_true_by_login(login=login)
    dataset = orm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'
    response = dm_api_facade.login.login_user(
        login=login,
        password=password)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())

