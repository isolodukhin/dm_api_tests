import requests


def post_v1_account():
    """
    Register new user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account"

    payload = {
        "login": "fkwekfewf",
        "email": "qwdwqd@dqwdq.com",
        "password": "aaaaadad"
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )
    return response
