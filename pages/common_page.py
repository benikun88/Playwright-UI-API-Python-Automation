from playwright.sync_api import Page

from pages.cart_page import CartPage


class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.locator("data-test=nav-sign-in")
        self.categories_drop_list = page.locator("data-test=nav-categories")
        self.mini_cart_button = page.locator("data-test=cart-quantity")
        # checkout flow
        self.proceed_to_checkout_button = page.locator("aw-wizard-step[steptitle='Cart'] button[type='button']")
        self.add_to_cart_successes_toast = page.locator(".toast-top-right.toast-container")

    def click_sign_in(self):
        self.sign_in_button.click()

    def click_cart_button(self):
        self.mini_cart_button.click()
        return CartPage(self.page)

