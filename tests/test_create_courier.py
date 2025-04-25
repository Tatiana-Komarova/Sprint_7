import pytest
import allure
import uuid
from methods.courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверка кода и ответа')
    def test_success_create_courier(self, generate_courier_data):
        response = CourierMethods.create_courier(generate_courier_data)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title('Содание двух одинаковых курьеров')
    @allure.description('Проверка кода и ответа')
    def test_create_duplicate_courier(self, generate_courier_data):
        body = generate_courier_data.copy()
        unique_suffix = uuid.uuid4().hex
        body['login'] = f"{body['login']}_{unique_suffix}"
        response_1 = CourierMethods.create_courier(body)
        assert response_1.status_code == 201
        response_2 = CourierMethods.create_courier(body)
        assert response_2.status_code == 409
        assert response_2.json().get('message') == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка создания курьера, если одного из обязательных полей нет ')
    @allure.description('Проверка кода и ответа')
    @pytest.mark.parametrize("missed_field", ["login", "password"])
    def test_create_courier_missing_field(self, generate_courier_data, missed_field):
        body = generate_courier_data.copy()
        body.pop(missed_field)
        response = CourierMethods.create_courier(body)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"
