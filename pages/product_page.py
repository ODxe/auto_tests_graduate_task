from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(By.XPATH, '//*[@value="Добавить в корзину"]')
        button.click()

