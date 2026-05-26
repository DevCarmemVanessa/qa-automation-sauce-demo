from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_adicionar_produto_ao_carrinho(driver):

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.acessar_site()
    login_page.preencher_usuario("standard_user")
    login_page.preencher_senha("secret_sauce")
    login_page.clicar_login()

    products_page.adicionar_produto_carrinho()

    assert products_page.obter_quantidade_carrinho() == "1"
