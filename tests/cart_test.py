import allure
import pytest
import time  # Don't forget to import the time module!
from playwright.sync_api import Page, expect
from pages.common_page import CommonPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


class TestCart:
    @pytest.fixture(autouse=True)
    @allure.description("setup login test")
    def setup_cart_test(self):
        self.main_page = MainPage(self.page)
        self.main_page.select_item_from_search("Pliers")
        self.product_page=ProductPage(self.page)
        self.product_page.add_to_cart()

    def test_success_add_to_cart(self):
        self.common_page=CommonPage(self.page)
        expect(self.common_page.add_to_cart_successes_toast).to_have_text("Product added to shopping cart.")
