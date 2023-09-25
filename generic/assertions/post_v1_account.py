import allure
from hamcrest import *
from generic.helpers.orm_db import OrmDatabase


class AssertionsPostV1Account:

    def __init__(self, orm_db):
        self.orm_db = orm_db

    def check_user_was_created(self, login):
        with allure.step("Проверка что пользователь был создан"):
            dataset = self.orm_db.get_user_by_login(login)
            for row in dataset:
                assert_that(row, has_entries(
                    {
                        "Login": login,
                        "Activated": False
                    }
                ))

    def check_user_was_activated(self, login):
        with allure.step("Проверка что пользователь был активирован"):
            dataset = self.orm_db.get_user_by_login(login=login)
            for row in dataset:
                assert row['Activated'] is True, f'User {login} not activated'
