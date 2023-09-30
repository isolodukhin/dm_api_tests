import allure
import pytest
from hamcrest import *
from string import ascii_letters, digits
import random


def random_string(count_of_symbols=8):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(count_of_symbols):
        string += random.choice(symbols)
    return string


@allure.suite("Тесты на проверку метода POST /v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:

    @pytest.mark.parametrize('login, email, password, status_code, check', [
        (random_string(3), '166132@12.ru', random_string(6), 201, ''),
        (random_string(3), '144@12.ru', random_string(5), 400, {"Password": ["Short"]}),
        (random_string(1), '153@12.ru', random_string(6), 400, {"Login": ["Short"]}),
        (random_string(3), '12@', random_string(6), 400, {"Email": ["Invalid"]}),
        (random_string(3), '12', random_string(6), 400, {"Email": ["Invalid"]}),
    ])
    def test_create_and_activated_user_with_random_params(
            self,
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
    def test_register_and_activate_user(self, dm_api_facade, orm_db, login, email, password, assertions):
        """
        Тест проверяет создание и активацию пользователя в базе данных
        :param dm_api_facade:
        :param orm_db:
        :param login:
        :param email:
        :param password:
        :param assertions:
        :return:
        """
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password)
        assertions.check_user_was_created(login=login)
        orm_db.set_user_activated_true_by_login(login=login)
        assertions.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(login=login, password=password)


    @allure.title("Проверка регистрации и активации пользователя")
    def test_create_and_activate_user_with_random_params_2(
            self,
            dm_api_facade,
            orm_db,
            prepare_user,
            assertions
    ):
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password
        dm_api_facade.account.register_new_user(login=login, email=email, password=password)
        assertions.check_user_was_created(login=login)
        orm_db.set_user_activated_true_by_login(login=login)
        assertions.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(login=login, password=password)


