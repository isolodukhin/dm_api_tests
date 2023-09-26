from common_libs.db_client import DbClient


class DmDataBase:
    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        query = 'select * from "public"."Users"'
        dataset = self.db.send_query(query=query)
        return dataset

    def get_user_by_login(self, login):
        query = f'''
        select * from "public"."Users"
        where "Login" = '{login}'
        '''
        dataset = self.db.send_query(query=query)
        return dataset

    def delete_user_by_login(self, login):
        query = f'''
        delete from "public"."Users"
        where "Login" = '{login}'
        '''
        dataset = self.db.send_bulk_query(query=query)
        return dataset

    def set_user_activated_true_by_login(self, login):
        query = f'''
        update "public"."Users" set "Activated" = 'True'
        where "public"."Users"."Login" = '{login}'
                '''
        self.db.send_bulk_query(query=query)


