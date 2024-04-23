from playwright.sync_api import Page


class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator(".product-title")
        self.quantity_field = page.locator("input[type='number']")
        self.price = page.locator("tbody tr td:nth-child(4) span:nth-child(1)")
        self.total_price = page.locator("tbody tr td:nth-child(4) span:nth-child(1)")
        self.remove_from_cart_button = page.locator(".btn.btn-danger")

    def change_quantity(self, quantity: str):
        self.quantity_field.fill(quantity)
