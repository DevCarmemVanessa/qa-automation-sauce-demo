from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_invalido():

    driver = webdriver.Edge()

    driver.get("https://www.saucedemo.com/")

    time.sleep(5)

    campo_usuario = driver.find_element(By.ID, "user-name")
    campo_senha = driver.find_element(By.ID, "password")
    botao_login = driver.find_element(By.ID, "login-button")

    campo_usuario.send_keys("usuario_errado")

    time.sleep(5)

    campo_senha.send_keys("senha_errada")

    time.sleep(5)

    botao_login.click()

    time.sleep(5)

    mensagem_erro = driver.find_element(By.TAG_NAME, "h3")

    assert "Epic sadface" in mensagem_erro.text

    driver.quit()
