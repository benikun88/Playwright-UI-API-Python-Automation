from faker import Faker


class HelperCommon:
    def __init__(self):
        self.fake = Faker()

    def generate_random_email(self):
        """Generate a random email address using faker."""
        return self.fake.email()
