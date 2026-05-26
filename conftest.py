from selenium import webdriver
import pytest

@pytest.fixture
def driver():

    driver = webdriver.Edge()

    yield driver

    driver.quit()
