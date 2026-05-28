from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_guest_can_go_to_login_page(browser):
    loginLink = browser.find_element(By.ID, "login_link")
    loginLink.click()

    time.sleep(30)