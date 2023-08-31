from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import RegistrationModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    token = mailhog.get_token_from_last_email()
    response = api.account.get_v1_account(token)


