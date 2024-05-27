import allure
import pytest
import time  # Don't forget to import the time module!
from playwright.sync_api import Page, expect

from configs.config_login import TEST_DATA
from pages.common_page import CommonPage
from pages.login_page import LoginPage


@allure.feature("Login")
class TestLogin:

    @pytest.fixture(autouse=True)
    @allure.description("setup login test")
    def setup_login_test(self):
        self.common_page = CommonPage(self.page)
        self.common_page.click_sign_in()
        self.login_page = LoginPage(self.page)

    @pytest.mark.devRun
    @pytest.mark.parametrize("email, password, expected_error", TEST_DATA)
    def test_login_with_cred(self, page: Page, email, password, expected_error):
        self.login_page.login_user(email, password)
        if expected_error:
            if expected_error == "Invalid email or password":
                expect(self.login_page.login_error).to_have_text(expected_error)
            elif expected_error == "Password is required":
                expect(self.login_page.password_error).to_have_text(expected_error)
            elif expected_error == "E-mail is required":
                expect(self.login_page.email_error).to_have_text(expected_error)
            else:
                # Handle any other specific error cases here
                pass
        else:
            expect(self.page).to_have_url("https://practicesoftwaretesting.com/#/account")
