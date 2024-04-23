from playwright.sync_api import Page


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator('#first_name')
        self.last_name_field = page.locator('#last_name')
        self.date_of_birth_field = page.locator('#dob')
        self.address_field = page.locator('#address')
        self.post_code_field = page.locator('#postcode')
        self.city_field = page.locator('#city')
        self.state_field = page.locator('#state')
        self.country_list = page.locator('#country')
        self.phone_field = page.locator('#phone')
        self.email_field = page.locator('#email')
        self.password_field = page.locator('#password')
        self.register_button = page.locator("button[type='submit']")
        # error msg's
        self.register_button = page.locator('data-test=postcode-error')

    def register(self, first_name: str, last_name: str, date_of_birth: str, password: str, address_field: str,
                 post_code_field: str
                 , state: str, country: str, city_field: str, phone: str, email: str):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.date_of_birth_field.fill(date_of_birth)
        self.address_field.fill(address_field)
        self.post_code_field.fill(post_code_field)
        self.city_field.fill(city_field)
        self.state_field.fill(state)
        self.country_list.select_option(country)
        self.phone_field.fill(phone)
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.register_button.click()
