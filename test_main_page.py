from selenium.webdriver.common.by import By
from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = f"http://selenium1py.pythonanywhere.com/en/"
    page = MainPage(browser, link)
    page.open()
    #page.go_to_main_page()
    page.should_be_login_link()