from selenium.webdriver.common.by import By
from pages.product_page import ProductPage

 
def test_guest_can_add_product_to_basket(browser):
    productPageLink = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    productPage = ProductPage(browser, productPageLink)
    productPage.open()

    productPage.add_to_cart()
    productPage.solve_quiz_and_get_code()