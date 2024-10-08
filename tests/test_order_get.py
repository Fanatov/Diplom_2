import API
import allure
from DATA import *


class TestOrderGet:
    @allure.title('Получение заказов авторизованного пользователя')
    @allure.description('Успешное получение списка заказов, соответствие статус-кода и ответа')
    def test_order_get_from_auth_user(self):
        access_token = API.user_login(StaticData.STATIC_USER).json()[Other.ACCESS_TOKEN]
        orders = API.order_get(headers={'Authorization': access_token})
        assert orders.status_code == StatusCodes.OK and orders.json()[Other.SUCCESS_JSON] is True

    @allure.title('Получение заказов неавторизованного пользователя')
    @allure.description('Проверка на ошибку, соответствие статус-кода и ответа')
    def test_order_get_from_not_auth_user(self):
        response = API.order_get(None)
        assert response.status_code == StatusCodes.UNAUTHORIZED and response.json()[Other.MESSAGE_JSON] == Responses.NOT_ALLOWED_AUTH
