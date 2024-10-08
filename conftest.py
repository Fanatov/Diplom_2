import pytest

import API
import genlogic
from genlogic import GeneratedPayloads


@pytest.fixture(scope='function')
def payloading():
    payload = genlogic.GeneratedPayloads().RANDOM_PAYLOAD
    response = API.user_create(payload)
    return response
