import allure
from playwright.sync_api import Page


class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_list = page.locator("select[aria-label='sort']")
        self.search_field = page.locator("data-test=search-query")
        self.search_submit = page.locator("data-test=search-submit")
        self.total_price = page.locator("tbody tr td:nth-child(4) span:nth-child(1)")
        self.remove_from_cart_button = page.locator(".btn.btn-danger")
        self.product_name = page.locator("data-test=product-name")
        self.reset_text_field = page.locator("data-test=search-reset")

    @allure.step("search for item: {item}")
    def search_item(self, item: str):
        self.search_field.fill(item)
        self.search_submit.click()

    @allure.step("reset the search field")
    def reset_search_field(self):
        self.reset_text_field.click()

    @allure.step("fill the search field")
    def fill_search_field(self, item: str):
        self.search_field.fill(item)
