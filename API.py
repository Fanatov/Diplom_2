import requests
from DATA import *


def user_create(data):
    response = requests.post(Urls.URL_MAIN + Api.CREATE_USER, json=data)
    return response


def user_login(data):
    response = requests.post(Urls.URL_MAIN + Api.LOGIN_USER, json=data)
    return response


def user_update(data, headers):
    response = requests.patch(Urls.URL_MAIN + Api.UPDATE_USER_INFO, json=data, headers=headers)
    return response


def user_delete(headers):
    response = requests.delete(Urls.URL_MAIN + Api.DELETE_USER, headers=headers)
    return response


def order_create(data, headers):
    response = requests.post(Urls.URL_MAIN + Api.CREATE_ORDER, json=data, headers=headers)
    return response


def order_get(headers):
    response = requests.get(Urls.URL_MAIN + Api.CREATE_ORDER, headers=headers)
    return response


def user_logout(data):
    response = requests.post(Urls.URL_MAIN + Api.LOGOUT_USER, data=data)
    return response
