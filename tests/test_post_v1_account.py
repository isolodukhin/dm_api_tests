import pytest
from dm_api_account.models.user_envelope_model import UserRole
from hamcrest import *
from string import ascii_letters, digits
import random


def random_string(count_of_symbols=8):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(count_of_symbols):
        string += random.choice(symbols)
    return string


@pytest.mark.parametrize('login, email, password, status_code, check', [
    (random_string(3), '16612@12.ru', random_string(6), 201, ''),
    (random_string(3), '144@12.ru', random_string(5), 400, {"Password": ["Short"]}),
    (random_string(1), '153@12.ru', random_string(6), 400, {"Login": ["Short"]}),
    (random_string(3), '12@', random_string(6), 400, {"Email": ["Invalid"]}),
    (random_string(3), '12', random_string(6), 400, {"Email": ["Invalid"]}),
])
def test_create_and_activated_user_with_random_params(
        dm_api_facade,
        orm_db,
        login,
        email,
        password,
        status_code,
        check
):
    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    if status_code == 201:
        dataset = orm_db.get_user_by_login(login)
        for row in dataset:
            assert_that(row, has_entries(
                {
                    "Login": login,
                    "Activated": False
                }
            ))
        orm_db.set_user_activated_true_by_login(login=login)
        dataset = orm_db.get_user_by_login(login=login)
        for row in dataset:
            assert row['Activated'] is True, f'User {login} not activated'
        dm_api_facade.login.login_user(
            login=login,
            password=password)
    else:
        error_message = response.json()['errors']
        assert_that(error_message, has_entries(check))
    orm_db.delete_user_by_login(login=login)


@pytest.mark.parametrize('login', [random_string() for _ in range(3)])
@pytest.mark.parametrize('email', [random_string() + '@' + random_string() + '.ru' for _ in range(3)])
@pytest.mark.parametrize('password', [random_string() for _ in range(3)])
def test_post_v1_account_2(dm_api_facade, orm_db, login, email, password):
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password)
    dataset = orm_db.get_user_by_login(login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                "Login": login,
                "Activated": False
            }
        ))
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
    orm_db.delete_user_by_login(login=login)


def test_post_v1_account(dm_api_facade, orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password)
    dataset = orm_db.get_user_by_login(login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                "Login": login,
                "Activated": False
            }
        ))
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
    orm_db.delete_user_by_login(login=login)
