from selenium.common.exceptions import NoSuchElementException

class BasePage():
    # конструктор — метод, который вызывается, когда мы создаем объект. 
    # Конструктор объявляется ключевым словом __init__
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # вспомогательный метод поиска элемента в нашей базовой странице 
    # BasePage, который будет возвращать нам True или False
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True