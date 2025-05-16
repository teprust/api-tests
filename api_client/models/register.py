from faker import Faker

fake = Faker()

class RegisterModel:

    def random(self):
        return {"login": fake.email(), "password": "aaaa"}