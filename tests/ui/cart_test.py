import time
import allure
import pytest
from playwright.sync_api import Page, expect

from configs.config_cart import PRODUCT_QUANTITY
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.common_page import CommonPage
from utilities.helper import HelperCommon

@allure.feature("Cart")
class TestCart:
    @pytest.fixture(autouse=True)
    @allure.description("Setup cart test")
    def setup_cart_test(self, page: Page):
        self.page = page
        self.main_page = MainPage(page)
        self.main_page.select_item_from_search("Pliers")
        self.product_page = ProductPage(page)
        self.product_page.add_to_cart()
        self.common_page = CommonPage(page)

    @allure.description("Verify that the product is successfully added to the cart")
    def test_success_add_to_cart(self, page: Page):
        expect(self.common_page.add_to_cart_successes_toast).to_have_text("Product added to shopping cart.")

    @allure.description("Check if the cart page displays the correct price for the product")
    def test_check_price_on_cart(self, page: Page):
        cart_page = self.common_page.click_cart_button()
        assert cart_page.price.text_content() == cart_page.total_price.text_content()

    @allure.description("Check if the cart page updates the total price correctly when the product quantity is changed")
    def test_check_price_multi_on_cart(self, page: Page):
        helper = HelperCommon()
        cart_page = self.common_page.click_cart_button()
        cart_page.change_quantity(PRODUCT_QUANTITY)
        time.sleep(4)
        assert helper.convert_and_multiply_price(cart_page.price.text_content(),
                                                 int(PRODUCT_QUANTITY)) == cart_page.total_price.text_content()

    @allure.description("Verify that the product is successfully removed from the cart")
    def test_success_remove_from_cart(self, page: Page):
        cart_page = self.common_page.click_cart_button()
        cart_page.click_remove_from_cart_button()
        expect(cart_page.product_title).to_be_hidden(timeout=3000)
