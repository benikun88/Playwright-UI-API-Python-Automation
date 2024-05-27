import allure
import pytest
import time  # Don't forget to import the time module!
from playwright.sync_api import Page, expect
from utilities.helper import HelperCommon
from configs.config_cart import PRODUCT_QUANTITY
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
        self.product_page = ProductPage(self.page)
        self.product_page.add_to_cart()

    def test_success_add_to_cart(self):
        self.common_page = CommonPage(self.page)
        expect(self.common_page.add_to_cart_successes_toast).to_have_text("Product added to shopping cart.")

    def test_check_price_on_cart(self):
        self.common_page = CommonPage(self.page)
        self.cart_page = self.common_page.click_cart_button()
        print(self.cart_page.price.text_content())
        print(self.cart_page.total_price.text_content())
        assert self.cart_page.price.text_content() == self.cart_page.total_price.text_content()

    def test_check_price_multi_on_cart(self):
        helper = HelperCommon()
        self.common_page = CommonPage(self.page)
        self.cart_page = self.common_page.click_cart_button()
        self.cart_page.change_quantity(PRODUCT_QUANTITY)
        time.sleep(4)
        assert helper.convert_and_multiply_price(self.cart_page.price.text_content(), int(PRODUCT_QUANTITY)) == self.cart_page.total_price.text_content()

    def test_success_remove_from_cart(self):
        self.common_page = CommonPage(self.page)
        self.cart_page = self.common_page.click_cart_button()
        self.cart_page.remove_from_cart()
        expect(self.cart_page.product_title).to_be_hidden(3)
