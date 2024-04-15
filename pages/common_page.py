from playwright.sync_api import Page


class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.locator(".nav-link[data-test='nav-sign-in']")

    def click_sign_in(self):
        self.sign_in_button.click()
