def test_put_v1_account_password(dm_api_facade, orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    new_password = "tests12345"
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
    dm_api_facade.account.reset_user_password(
        login=login,
        email=email
    )
    token = dm_api_facade.mailhog.get_reset_password_token_by_login(login=login)
    dm_api_facade.account.change_user_password(
        login=login,
        token=token,
        old_password=password,
        new_password=new_password)


