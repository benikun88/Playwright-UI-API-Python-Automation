import allure
from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator(".product-title")
        self.quantity_field = page.locator("input[type='number']")
        self.price = page.locator("tbody tr[class='ng-star-inserted'] td:nth-child(3) span:nth-child(1)")
        self.total_price = page.locator("td:nth-child(4) span:nth-child(1)")
        self.remove_from_cart_button = page.locator(".btn.btn-danger")

    @allure.step("change cart quantity")
    def change_quantity(self, quantity: str):
        self.quantity_field.fill(quantity)
        self.quantity_field.press("Enter")

    @allure.step("click remove item from cart")
    def click_remove_from_cart_button(self):
        self.remove_from_cart_button.click()