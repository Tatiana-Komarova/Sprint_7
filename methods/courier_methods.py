import requests
import data
import allure


class CourierMethods:
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(body):
        return requests.post(f'{data.Url.BASE_URL}{data.Url.CREATE_COURIER_URL}', json=body)

    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(login: str = None, password: str = None):
        body = {}
        if login is not None:
            body["login"] = login
        if password is not None:
            body["password"] = password
        return requests.post(f'{data.Url.BASE_URL}{data.Url.COURIER_LOGIN_URL}', json=body)

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        return requests.delete(f'{data.Url.BASE_URL}{data.Url.CREATE_COURIER_URL}/{courier_id}')