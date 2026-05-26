from selenium import webdriver

def test_login():

    driver = webdriver.Edge()

    driver.get("https://www.saucedemo.com/")

    assert "saucedemo" in driver.current_url

    driver.quit()
