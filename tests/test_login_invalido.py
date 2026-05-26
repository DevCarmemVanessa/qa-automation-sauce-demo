from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_invalido():

    driver = webdriver.Edge()

    login_page = LoginPage(driver)

    login_page.acessar_site()
    login_page.preencher_usuario("usuario_errado")
    login_page.preencher_senha("senha_errada")
    login_page.clicar_login()

    mensagem_erro = driver.find_element(By.TAG_NAME, "h3")

    assert "Epic sadface" in mensagem_erro.text

    driver.quit()
