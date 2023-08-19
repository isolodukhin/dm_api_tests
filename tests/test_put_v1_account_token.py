from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    response = api.account.put_v1_account_token(
        token='1491c43a-ec88-40a5-81e9-76094e15786e'
    )
    print(response)
