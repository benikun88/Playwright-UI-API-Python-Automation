import os
import shutil
import pytest
import allure
from applitools.images import Eyes
from playwright.sync_api import sync_playwright, Browser, Page
from _pytest.config import Config


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    playwright.selectors.set_test_id_attribute("data-test")
    yield browser
    browser.close()


@pytest.fixture()
def context(browser, tmpdir):
    video_path = os.path.join(tmpdir, "videos")
    os.makedirs(video_path, exist_ok=True)
    context = browser.new_context(record_video_dir=video_path)
    yield context
    context.close()


@pytest.fixture()
def page(context: Browser):
    page = context.new_page()
    page.goto("https://practicesoftwaretesting.com")
    yield page
    page.close()


@pytest.fixture(autouse=True)
def setup(request, playwright, page):
    if "api" not in request.node.keywords:
        yield None
    else:
        yield None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and "api" not in item.keywords:
        page = item.funcargs.get('page', None)
        if page:
            video_path = page.video.path() if page.video else None
            if video_path:
                page.context.close()  # Ensure the context is closed to finalize the video
                if os.path.exists(video_path) and os.path.getsize(video_path) > 0:
                    with open(video_path, 'rb') as video_file:
                        allure.attach(video_file.read(), name="video", attachment_type=allure.attachment_type.MP4)


def pytest_configure(config: Config) -> None:
    allure_results_dir = "allure-results"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir)
    config.option.allure_report_dir = allure_results_dir


@pytest.fixture()
def eyes():
    eyes = Eyes()
    eyes.api_key = 'yQZoWxzsvOfSFbrd3YGmcSpl1061UWFGuNz6dXPWMQvXA110'  # Set your Applitools API key here

