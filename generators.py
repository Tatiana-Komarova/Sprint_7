from faker import Faker
fake = Faker()


def generate_courier_body():
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }

def generate_order_body():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.street_address(),
        "metroStation": fake.random_int(1,15),
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(1, 7),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment": fake.sentence(6)}