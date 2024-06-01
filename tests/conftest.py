
import os
import pytest
import allure
from applitools.images import Eyes
from playwright.sync_api import sync_playwright
from _pytest.config import Config


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture()
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    playwright.selectors.set_test_id_attribute("data-test")
    yield browser
    browser.close()


@pytest.fixture()
def page(browser):
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com")
    yield page
    page.close()


@pytest.fixture(autouse=True)
def setup(request, playwright, page):
    if "api" not in request.node.keywords:
        yield None
    else:
        yield None


def pytest_exception_interact(node, call, report):
    if report.failed:
        if "api" not in report.keywords:
            page = node.instance.page
            screenshot = page.screenshot()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)


def pytest_configure(config: Config) -> None:
    config.option.allure_report_dir = "allure-results"


@pytest.fixture()
def eyes():
    eyes = Eyes()
    eyes.api_key = 'yQZoWxzsvOfSFbrd3YGmcSpl1061UWFGuNz6dXPWMQvXA110'  # Set your Applitools API key here
    yield eyes
    eyes.abort_async()
