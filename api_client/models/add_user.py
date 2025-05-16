from faker import Faker

fake = Faker()

class AddUserModel:

    def random(self):
        return {
            "name": "str",
            "age": 0,
            "gender": None,
            "date_registration": None,
            "is_active": True
        }