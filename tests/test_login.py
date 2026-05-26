from selenium import webdriver
from pages.login_page import LoginPage

def test_login_valido():

    driver = webdriver.Edge()

    login_page = LoginPage(driver)

    login_page.acessar_site()
    login_page.preencher_usuario("standard_user")
    login_page.preencher_senha("secret_sauce")
    login_page.clicar_login()

    assert "inventory" in driver.current_url

    driver.quit()
