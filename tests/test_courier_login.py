import allure
import pytest
from methods.courier_methods import CourierMethods

@allure.title('Проверка логина курьера')
class TestLoginCourier:
    @allure.step('Проверка авторизации курьера')
    @allure.description('Проверка кода и ответа')
    def test_login_success(self, generate_courier_data):
        courier = CourierMethods.create_courier(generate_courier_data)

        assert courier.status_code == 201

        response = CourierMethods.login_courier(generate_courier_data["login"], generate_courier_data["password"])

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.step('Проверка авторизации курьера, если одно из полей не заполнено')
    @allure.description('Проверка кода и ответа')
    @pytest.mark.parametrize("missed_field", ["login", "password"])
    def test_login_missing_field(self, generate_courier_data, missed_field):
        CourierMethods.create_courier(generate_courier_data)
        response = CourierMethods.login_courier(None, generate_courier_data["password"])

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"

    @allure.step('Проверка авторизации курьера с несуществующим логином')
    @allure.description('Проверка кода и ответа')
    def test_login_nonexist(self):
        response = CourierMethods.login_courier("no_such_login", "no_such_pass")

        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.step('Проверка авторизации курьера')
    @allure.description('Проверка кода и ответа с неверным паролем')
    def test_login_wrong_password(self, generate_courier_data):
        CourierMethods.create_courier(generate_courier_data)
        response = CourierMethods.login_courier(generate_courier_data["login"], generate_courier_data["password"] + "_WRONG")

        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"