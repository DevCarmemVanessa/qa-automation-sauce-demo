from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_valido():

    driver = webdriver.Edge()

    driver.get("https://www.saucedemo.com/")

    campo_usuario = driver.find_element(By.ID, "user-name")
    campo_senha = driver.find_element(By.ID, "password")
    botao_login = driver.find_element(By.ID, "login-button")

    campo_usuario.send_keys("standard_user")
    campo_senha.send_keys("secret_sauce")
    botao_login.click()

    assert "inventory" in driver.current_url

    driver.quit()
