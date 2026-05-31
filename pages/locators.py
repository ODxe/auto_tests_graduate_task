from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    LOGIN_LINK = (By.ID, 'login_link')

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn btn-lg btn-primary btn-add-to-basket')