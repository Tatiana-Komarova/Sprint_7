import requests
import data
import allure

class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order_data):
        body = order_data.copy()
        if "color" in body and isinstance(body["color"], str):
            body["color"] = [body["color"]]
        return requests.post(f"{data.Url.BASE_URL}{data.Url.ORDER_CREATE_URL}", json=body)


    @staticmethod
    @allure.step('Получение списка заказов')
    def get_orders():
        return requests.get(f"{data.Url.BASE_URL}{data.Url.ORDER_LIST_URL}")