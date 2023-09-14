from dm_api_account.models.user_envelope_model import UserRole
from hamcrest import *


def test_post_v1_account_email(dm_api_facade, orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    new_email = '1s738511211@dqwdq.com'
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
    response = dm_api_facade.account.change_user_email(
        login=login,
        password=password,
        email=new_email
    )
    assert_that(response.resource, has_properties(
        {
            "login": "fkw76fewf4982111",
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())
    orm_db.delete_user_by_login(login=login)


