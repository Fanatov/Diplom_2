import API
import allure
import genlogic
from DATA import *


class TestUpdateUser:
    @allure.title('Проверка изменения данных авторизованного пользователя - Все поля')
    @allure.description('Проверка на изменения данных, сооветствия статус-кода и ответа')
    def test_auth_user_update(self, payloading):
        user = payloading
        access_token = user.json()[Other.ACCESS_TOKEN]
        response = API.user_update(genlogic.GeneratedPayloads().RANDOM_PAYLOAD, headers={'Authorization': access_token})
        assert response.status_code == StatusCodes.OK and response.json()[Other.SUCCESS_JSON] is True
        API.user_delete(headers={'Authorization': access_token})

    @allure.title('Проверка изменения данных неавторизованного пользователя')
    @allure.description('Проверка на ошибку, сооветствие статус-кода и ответа')
    def test_not_auth_user_update(self):
        response = API.user_update(genlogic.GeneratedPayloads().RANDOM_PAYLOAD, headers=None)
        assert response.status_code == StatusCodes.UNAUTHORIZED and response.json()[Other.MESSAGE_JSON] == Responses.NOT_ALLOWED_AUTH

    @allure.title('Проверка изменения данных авторизованного пользователя - E-Mail')
    @allure.description('Проверка на изменения данных, сооветствия статус-кода и ответа')
    def test_auth_user_update_email(self, payloading):
        user = payloading
        access_token = user.json()[Other.ACCESS_TOKEN]
        response = API.user_update(genlogic.GeneratedPayloads().MAIL_ONLY, headers={'Authorization': access_token})
        assert user.json()['user']['email'] != response.json()['user']['email']
        API.user_delete(headers={'Authorization': access_token})

    @allure.title('Проверка изменения данных авторизованного пользователя - Имя')
    @allure.description('Проверка на изменения данных, сооветствия статус-кода и ответа')
    def test_auth_user_update_name(self, payloading):
        user = payloading
        access_token = user.json()[Other.ACCESS_TOKEN]
        response = API.user_update(genlogic.GeneratedPayloads().NAME_ONLY, headers={'Authorization': access_token})
        assert user.json()['user']['name'] != response.json()['user']['name']
        API.user_delete(headers={'Authorization': access_token})

    @allure.title('Проверка изменения данных авторизованного пользователя - Пароль')
    @allure.description('Проверка на изменения данных, сооветствия статус-кода и ответа')
    def test_auth_user_update_password(self):
        correct_user = genlogic.GeneratedPayloads()
        user_filled = correct_user.RANDOM_PAYLOAD
        old_password = user_filled['password']
        new_password = correct_user.create_random_password()
        API.user_create(user_filled)
        user = API.user_login(user_filled)
        access_token = user.json()[Other.ACCESS_TOKEN]
        refresh_token = user.json()[Other.REFRESH_TOKEN]
        user_filled['password'] = new_password
        API.user_update(user_filled, headers={'Authorization': access_token})
        API.user_logout(data={"token": refresh_token})
        user_filled['password'] = old_password
        old_password_attempt = API.user_login(user_filled)
        user_filled['password'] = new_password
        new_password_attempt = API.user_login(user_filled)
        assert old_password_attempt.json()[Other.SUCCESS_JSON] is False and new_password_attempt.json()[
            Other.SUCCESS_JSON] is True
