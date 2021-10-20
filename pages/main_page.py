import time
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys

link = "https://yandex.ru/"

class MainPage(BasePage):
    def is_tensor_ru_in_top_five_search_results(self):
        self.go_to_yandex_ru()
        time.sleep(1)
        self.should_be_search_box()
        time.sleep(1)
        self.input_tensor_to_search_box()
        time.sleep(1)
        self.does_suggest_appear()
        time.sleep(1)
        self.hit_enter_on_search_box()
        time.sleep(1)
        self.is_tensor_in_top_5_results()
        time.sleep(1)

    # 1) Зайти на yandex.ru
    def go_to_yandex_ru(self):
        self.browser.get(link)

    # 2) Проверить наличия поля поиска
    def should_be_search_box(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_BOX), "Search box is not on the page"

    # 3) Ввести в поиск Тензор
    def input_tensor_to_search_box(self):
        global search_box
        search_box = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        search_box.send_keys("тензор")

    # 4) Проверить, что появилась таблица с подсказками (suggest)
    def does_suggest_appear(self):
        assert self.is_element_present(*MainPageLocators.SUGGESTS_TABLE), "Suggest table is not on the page"

    # 5) При нажатии Enter появляется таблица результатов поиска
    def hit_enter_on_search_box(self):
        search_box.send_keys(Keys.ENTER)
        current_url = self.browser.current_url
        assert "https://yandex.ru/search/" in current_url, "Results table doesn't show up"

    # 6) В первых 5 результатах есть ссылка на tensor.ru
    def is_tensor_in_top_5_results(self):
        search_results = self.browser.find_elements(*MainPageLocators.SEARCH_RESULTS)
        search_results_text = [i.text for i in search_results]
        assert "tensor.ru" in search_results_text, "'tensor.ru' is not in top 5 results"

