from faker import Faker

fake = Faker('ru_RU')

fake_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}