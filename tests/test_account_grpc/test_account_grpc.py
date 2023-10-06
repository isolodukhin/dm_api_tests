import pytest

from apis.dm_api_account_async import RegisterAccountRequest


def test_register_account(grpc_account, prepare_user):
    response = grpc_account.register_account(
        login=prepare_user.login,
        email=prepare_user.email,
        password=prepare_user.password
    )


@pytest.mark.asyncio
async def test_register_account_async(grpc_account_async, prepare_user):
    response = await grpc_account_async.register_account(
        register_account_request=RegisterAccountRequest(
            login=prepare_user.login,
            email=prepare_user.email,
            password=prepare_user.password
        )
    )
    print(response.to_dict())
