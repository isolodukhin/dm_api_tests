import pytest
from generic.helpers.orm_db import OrmDatabase
from services.dm_api_account import Facade
import structlog
from generic.helpers.mailhog import MailhogApi
from collections import namedtuple

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def mailhog():
    return MailhogApi(host='http://5.63.153.31:5025')


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(host='http://5.63.153.31:5051', mailhog=mailhog)


@pytest.fixture
def orm_db():
    orm = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    yield orm
    orm.db.close_connection()

@pytest.fixture
def prepare_user():
    user = namedtuple('User', 'login, email, password')
    User = user(
        login="log_in_104",
        email='log_in_104@dqwdq.com',
        password='aaaaadad')
    return User