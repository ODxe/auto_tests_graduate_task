class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    #конструктор для неявного ожидания
    def __int__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
    
    #перехват исключения на присутствие элемента
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True