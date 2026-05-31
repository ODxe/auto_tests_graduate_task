from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_main_page(browser):
    mainPageLink = f"http://selenium1py.pythonanywhere.com/"
    mainPage = MainPage(browser, mainPageLink)

    mainPage.go_to_main_page()

def test_check_login_page(browser):
    loginPageLink = f"http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    loginPage = LoginPage(browser, loginPageLink)
    loginPage.open()

    loginPage.should_be_login_url()
    loginPage.should_be_login_form()
    loginPage.should_be_register_form()