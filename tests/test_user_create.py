import API
import allure

import genlogic
from DATA import *


class TestUserCreate:
    @allure.title('Успешное создание пользователя')
    @allure.description('Проверка на успешное создание юзера, соответствия статус-кода и ответа')
    def test_user_create(self):
        user = API.user_create(genlogic.GeneratedPayloads().RANDOM_PAYLOAD)
        access_token = user.json()[Other.ACCESS_TOKEN]
        assert user.status_code == StatusCodes.OK and user.json()[Other.SUCCESS_JSON] is True
        API.user_delete(headers={'Authorization': access_token})

    @allure.title('Отсутствие возможности создания двух одинаковых пользователей')
    @allure.description('Проверка на ошибку, соответствия статус-кода и ответа')
    def test_user_duplicate(self):
        user = API.user_create(StaticData.STATIC_USER)
        assert user.status_code == StatusCodes.FORBIDDEN and user.json()[Other.MESSAGE_JSON] == Responses.USER_EXISTING

    @allure.title('Заполнение полей')
    @allure.description('Проверка на ошибку, соответствие статус-кода и ответа')
    def test_user_create_required_fields(self):
        user = API.user_create(genlogic.GeneratedPayloads().MAIL_PASS_ONLY)
        assert user.status_code == StatusCodes.FORBIDDEN and user.json()[Other.MESSAGE_JSON] == Responses.REQUIRING_FIELDS