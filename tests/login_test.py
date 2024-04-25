import pytest
import time  # Don't forget to import the time module!
from playwright.sync_api import Page, expect
from pages.common_page import CommonPage
from pages.login_page import LoginPage


class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_login_test(self):
        self.common_page = CommonPage(self.page)
        self.common_page.click_sign_in()
        self.login_page = LoginPage(self.page)

    @pytest.mark.devRun
    def test_01(self, page: Page):
        self.login_page.login_user("customer@practicesoftwaretesting.com", "welcome01")
        expect(self.page).to_have_url("https://practicesoftwaretesting.com/#/account")
