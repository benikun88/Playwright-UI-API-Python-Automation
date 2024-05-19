import allure
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.locator('#email')
        self.password_field = page.locator('#password')
        self.login_button = page.locator("input[value='Login']")
        self.register_button = page.locator("a[data-test='register-link']")
        self.forgot_password_button = page.locator(".ForgetPwd")
        # self.login_error = page.locator("data-test=login-error")
        self.login_error = page.get_by_test_id("login-error")
        self.password_error = page.locator("data-test=password-error")
        self.email_error = page.locator("data-test=email-error")

    @allure.step("user login with cred - email: {email}, password: {password}")
    def login_user(self, email: str, password: str):
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.login_button.click()
