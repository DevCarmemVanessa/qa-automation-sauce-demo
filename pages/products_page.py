from selenium.webdriver.common.by import By

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def adicionar_produto_carrinho(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def obter_quantidade_carrinho(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
