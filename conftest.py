import pytest

import API
import genlogic
from genlogic import GeneratedPayloads


@pytest.fixture
def payloading():
    payload = genlogic.GeneratedPayloads().RANDOM_PAYLOAD
    response = API.user_create(payload)
    return response
