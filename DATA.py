class Urls:
    URL_MAIN = 'https://stellarburgers.nomoreparties.site/'


class Api:
    CREATE_ORDER = f'api/orders'
    RESET_PASSWORD = f'api/password-reset'
    CREATE_USER = f'api/auth/register'
    LOGOUT_USER = f'api/auth/logout'
    LOGIN_USER = f'api/auth/login'
    TOKEN_UPDATE = f'api/auth/token'
    UPDATE_USER_INFO = f'api/auth/user'
    DELETE_USER = f'api/auth/user'
    GET_ALL_ORDERS = f'/api/orders/all'


class Responses:
    USER_EXISTING = f'User already exists'
    REQUIRING_FIELDS = f'Email, password and name are required fields'
    INCORRECT_MAIL_PASS = f'email or password are incorrect'
    EXISTING_MAIL = f'User with such email already exists'
    NOT_ALLOWED_AUTH = f'You should be authorised'
    EMPTY_INGRIDIENTS_ID = f'Ingredient ids must be provided'


class StaticData:
    STATIC_USER = {
        "email": "uyghnbnvbvrsadsarrrr@a.ru",
        "password": "12345678",
        "name": "fgdgdgdfgdfg"
    }

class Other:
    ACCESS_TOKEN = f'accessToken'
    SUCCESS_JSON = f'success'
    MESSAGE_JSON = f'message'
    FAIL_INGRIDIENTS_DATA = {
        "ingredients": ["1sss", "609646e4dc916e00276b2870"]}
    SUCCESS_INGRIDIENTS_DATA = {
        "ingredients": ["61c0c5a71d1f82001bdaaa73", "61c0c5a71d1f82001bdaaa6e"]
    }
    EMPTY_INGRIDIENTS_FIELD_DATA = {"ingredients": ""}

class StatusCodes:
    OK = 200
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    INTERNAL_ERROR = 500
    FORBIDDEN = 403