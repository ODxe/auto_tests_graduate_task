from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    #открытие страницы
    def go_to_main_page(self):
        loginLink = self.browser.find_element(By.ID, "login_link")
        loginLink.click()

    #проверка на корректность ссылки логина
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"