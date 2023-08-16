import requests


def put_v1_account_password():
    """
    Change registered user password
    :return:
    """
    token = '1142'
    url = "http://5.63.153.31:5051/v1/account/password"

    payload = {
      "login": "fewfwe",
      "token": f"{token}",
      "oldPassword": "12345679",
      "newPassword": "123456793"
    }
    headers = {
      'X-Dm-Auth-Token': '',
      'X-Dm-Bb-Render-Mode': '',
      'Content-Type': 'application/json',
      'Accept': 'text/plain'
    }

    response = requests.request(
      method="PUT",
      url=url,
      headers=headers,
      json=payload
    )
    return response
