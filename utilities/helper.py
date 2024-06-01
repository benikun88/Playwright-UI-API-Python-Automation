from faker import Faker


class HelperCommon:
    def __init__(self):
        self.fake = Faker()

    def navigate_to(self, url):
        self.page.goto(url)

    def generate_random_email(self):
        """Generate a random email address using faker."""
        return self.fake.email()

    def convert_and_multiply_price(self, price_string, multiplier):
        """
        Convert a price string to a float, multiply it, and return a formatted string with a dollar sign.

        :param price_string: The price string to be converted (e.g., "$12.01").
        :param multiplier: The multiplier to apply to the price.
        :return: The formatted price string after multiplication (e.g., "$24.02").
        """
        price_number = float(price_string.replace("$", ""))
        multiplied_price = price_number * multiplier
        return f"${multiplied_price:.2f}"
