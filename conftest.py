from selenium import webdriver
import pytest

@pytest.fixture
def driver(request):

    driver = webdriver.Edge()

    yield driver

    if request.node.rep_call.failed:

        driver.save_screenshot(f"screenshots/{request.node.name}.png")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
