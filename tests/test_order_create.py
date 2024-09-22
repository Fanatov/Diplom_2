import API
import allure
from DATA import *


class TestOrderCreate:
    @allure.title('Создание заказа авторизованным пользователем')
    @allure.description('Проверка на успешное создания заказа, соответствие статус-кода и ответа')
    def test_order_create_auth_user(self):
        access_token = API.user_login(StaticData.STATIC_USER).json()[Other.ACCESS_TOKEN]
        response = API.order_create(data=Other.SUCCESS_INGRIDIENTS_DATA, headers={'Authorization': access_token})
        assert response.status_code == StatusCodes.OK and response.json()[Other.SUCCESS_JSON] is True

    ### Баг. Обратиться к Иксанову Камилу, руководителю текущей когорты.
    @allure.title('Создание заказа неавторизованным пользователем')
    @allure.description('Проверка на ошибку, соответствие статус-кода и ответа')
    def test_order_create_not_auth_user(self):
        response = API.order_create(data=Other.SUCCESS_INGRIDIENTS_DATA, headers=None)
        assert response.status_code == StatusCodes.UNAUTHORIZED and response.json()[Other.MESSAGE_JSON] == Responses.NOT_ALLOWED_AUTH

    @allure.title('Создание заказа с ингредиентами')
    @allure.description('Проверка на ошибку, соответствие статус-кода и ответа')
    def test_order_create_with_ingridients(self):
        response = API.order_create(data=Other.SUCCESS_INGRIDIENTS_DATA, headers=None)
        assert response.status_code == StatusCodes.OK and response.json()[
            Other.SUCCESS_JSON] is True

    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Проверка на ошибку, соответствие статус-кода и ответа')
    def test_order_create_without_ingridients(self):
        response = API.order_create(data=Other.EMPTY_INGRIDIENTS_FIELD_DATA, headers=None)
        assert response.status_code == StatusCodes.BAD_REQUEST and response.json()[Other.MESSAGE_JSON] == Responses.EMPTY_INGRIDIENTS_ID

    @allure.title('Создание заказа с некорректным хешем ингредиента')
    @allure.description('Проверка на ошибку, соответствие статус-кода')
    def test_order_create_incorrect_ingridients(self):
        response = API.order_create(data=Other.FAIL_INGRIDIENTS_DATA, headers=None)
        assert response.status_code == StatusCodes.INTERNAL_ERROR
