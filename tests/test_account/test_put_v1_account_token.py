from hamcrest import *
from dm_api_account.models.user_envelope_model import UserRole


def test_put_v1_account_token(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password)
    response = dm_api_facade.account.activate_registered_user(login=login)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
    assert_that(response.resource.rating, not_none())
