from sqlalchemy import select, delete, update
from typing import List

from common_libs.orm_client.orm_client import OrmClient
from generic.helpers.orm_models import User
import allure

class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    def get_all_users(self):
        with allure.step("Get all users from DB"):
            query = select([User])
            dataset = self.db.send_query(query)
        return dataset

    def get_user_by_login(self, login) -> List[User]:
        with allure.step("Get user by login from DB"):
            query = select([User]).where(
                User.Login == login
            )
            dataset = self.db.send_query(query)
        return dataset

    def delete_user_by_login(self, login):
        with allure.step("Delete user from DB"):
            query = delete(User).where(
                User.Login == login
            )
            dataset = self.db.send_bulk_query(query=query)
        return dataset

    def set_user_activated_true_by_login(self, login, is_activate: bool = True):
        with allure.step("Set user activated true in DB"):
            query = update(User).where(
                User.Login == login
            ).values(
                {
                    User.Activated: is_activate
                }
            )
            dataset = self.db.send_bulk_query(query)
        return dataset
