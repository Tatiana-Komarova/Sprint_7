import pytest
import allure
from methods.order_methods import OrderMethods


@allure.title('Проверка создания заказа')
class TestOrders:
    @allure.step('Проверка создания заказа с одним цветом, двумя цветами или без цвета')
    @allure.description('Проверка кода и ответа')
    @pytest.mark.parametrize("colors", ["BLACK", "GREY", ["BLACK", "GREY"], None])
    def test_create_order_with_various_colors(self, generate_order_data, colors):
        order_body = generate_order_data(colors)
        response = OrderMethods.create_order(order_body)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.step('Проверка списка заказа')
    @allure.description('Проверка кода и ответа')
    def test_get_orders_list(self):
        response = OrderMethods.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
