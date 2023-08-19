import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "fkwek3fewf",
        "email": "qwdwqd3@dqwdq.com",
        "password": "aaaaadad"
    }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)
