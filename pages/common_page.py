from playwright.sync_api import Page


class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.locator(".nav-link[data-test='nav-sign-in']")
        self.mini_cart_button = page.locator("data-test=cart-quantity")
        # checkout flow
        self.proceed_to_checkout_button = page.locator("aw-wizard-step[steptitle='Cart'] button[type='button']")

    def click_sign_in(self):
        self.sign_in_button.click()
