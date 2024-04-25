from playwright.sync_api import Page


class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_list = page.locator("select[aria-label='sort']")
        self.search_field = page.locator("data-test=search-query")
        self.search_submit = page.locator("data-test=search-submit")
        self.total_price = page.locator("tbody tr td:nth-child(4) span:nth-child(1)")
        self.remove_from_cart_button = page.locator(".btn.btn-danger")
