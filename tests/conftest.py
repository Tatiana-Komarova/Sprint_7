from generators import generate_courier_body
from generators import generate_order_body
from methods.courier_methods import CourierMethods
from faker import Faker
import pytest
fake = Faker()


@pytest.fixture(scope="class")
def generate_courier_data():
    courier_body = generate_courier_body()
    yield courier_body
    login_response = CourierMethods.login_courier(courier_body["login"], courier_body["password"])
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        CourierMethods.delete_courier(courier_id)



@pytest.fixture
def generate_order_data():
    order_body = generate_order_body()
    def _builder(colors):
        body = order_body.copy()
        if colors is not None:
            body["color"] = colors if isinstance(colors, list) else [colors]
        return body
    return _builder