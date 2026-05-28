from selenium import webdriver
import pytest 

def pytest_addoption(parser):
    parser.addoption('--language')

def enter_language():
    print('Примечание: при отсутствии введенного значения будет установлен стандартный язык - en')
    language = input('Введите язык приложения: ')
    return language

@pytest.fixture()
def browser():
    domainLanguage = enter_language()
    if domainLanguage == "":
        domainLanguage = 'en'
        
    browser = webdriver.Chrome()
    link = f"http://selenium1py.pythonanywhere.com/{domainLanguage}/"
    browser.get(link)

    yield browser
    browser.quit()