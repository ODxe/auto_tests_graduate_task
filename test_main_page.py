from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    # mainPageLink = f"http://selenium1py.pythonanywhere.com/"
    loginPageLink = f"http://selenium1py.pythonanywhere.com/ru/accounts/login/" 

    #page = MainPage(browser, mainPageLink)
    loginPage = LoginPage(browser, loginPageLink)
    loginPage.open()

    #page.go_to_main_page()
    #page.should_be_login_link()

    loginPage.should_be_login_url()
    loginPage.should_be_login_form()
    loginPage.should_be_register_form()
