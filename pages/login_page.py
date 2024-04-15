from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        # super().__init__(page)
        self.page = page
        self.email_field = page.locator('#email')
        self.password_field = page.locator('#password')
        self.login_Button = page.locator("input[value='Login']")

    def login_user(self, username: str, password: str):
        self.email_field.fill(username)
        self.password_field.fill(password)
        self.login_Button.click()
