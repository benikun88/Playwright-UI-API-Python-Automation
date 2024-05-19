import allure
from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator('data-test=add-to-cart')
        self.increase_quantity_button = page.locator('data-test=increase-quantity')
        self.decrease_quantity_button = page.locator('data-test=decrease-quantity')
        self.product_name = page.locator('data-test=product-name')

    def add_to_cart(self):
        self.add_to_cart_button.click()
