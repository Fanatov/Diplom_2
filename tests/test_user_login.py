import API
import allure
from DATA import *


class TestUserLogin:
    @allure.title('Проверка на успешный логин под существующим пользователем')
    @allure.description('Проверка успешного логина, соответствие статус-кода и ответа')
    def test_user_login_success(self):
        response = API.user_login(StaticData.STATIC_USER_LOGIN)
        assert response.status_code == StatusCodes.OK and response.json()[Other.SUCCESS_JSON] is True

    @allure.title('Проверка на логин не существующим пользователем')
    @allure.description('Проверка на ошибку, соответствие статус-кода и ответа')
    def test_user_non_existing_user_fail(self):
        response = API.user_login(StaticData.STATIC_FAIL_USER_LOGIN)
        assert response.status_code == StatusCodes.UNAUTHORIZED and response.json()[
            Other.MESSAGE_JSON] == Responses.INCORRECT_MAIL_PASS
