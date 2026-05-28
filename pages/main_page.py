from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_main_page(self):
        loginLink = self.browser.find_element(By.ID, "login_link")
        loginLink.click()