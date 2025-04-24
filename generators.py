from faker import Faker
fake = Faker()


def generate_courier_body():
    return {
        "login": fake.user_name(),
        "password": fake.password(),
        "firstName": fake.first_name()
    }