from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    #открытие страницы
    def go_to_main_page(self):
        loginLink = self.browser.find_element(By.ID, "login_link")
        loginLink.click()

    #проверка на корректность ссылки логина
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"