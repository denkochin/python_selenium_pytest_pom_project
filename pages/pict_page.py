import time
from .base_page import BasePage
from .locators import PictPageLocators
from selenium.webdriver.common.keys import Keys

link = "https://yandex.ru/"

class PictPage(BasePage):
    def does_pictures_page_work(self):
        self.go_to_yandex_ru()
        time.sleep(1)
        self.should_be_pictures_link()
        time.sleep(1)
        self.click_the_pictures_link()
        time.sleep(1)
        self.check_the_pictures_page_url()
        time.sleep(1)
        self.open_first_category_and_check_the_opening()
        time.sleep(1)
        self.open_first_picture_and_check()
        time.sleep(1)
        self.click_next_picture_button()
        time.sleep(1)
        self.click_previous_picture_button()
        time.sleep(1)

    # 1) Зайти на yandex.ru
    def go_to_yandex_ru(self):
        self.browser.get(link)

    # 2) Ссылка «Картинки» присутствует на странице
    def should_be_pictures_link(self):
        assert self.is_element_present(*PictPageLocators.PICTURES_LINK), "Pictures link is not on the page"

    # 3) Кликаем на ссылку
    def click_the_pictures_link(self):
        self.browser.find_element(*PictPageLocators.PICTURES_LINK).click()

    # 4) Проверить, что перешли на url https://yandex.ru/images/
    def check_the_pictures_page_url(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        current_url = self.browser.current_url
        assert "https://yandex.ru/images/" in current_url, "Results table doesn't show up" 
    
    # 5) Открыть 1 категорию, проверить что открылась, в поиске верный текст
    def open_first_category_and_check_the_opening(self):
        category_name = self.browser.find_element(*PictPageLocators.FIRST_CATEGORY_NAME).get_attribute("data-grid-text")
        self.browser.find_element(*PictPageLocators.FIRST_CATEGORY).click()
        input = self.browser.find_element(*PictPageLocators.SEARCH_BOX_UNIQ)
        input_value = input.get_attribute('value')
        assert input_value == category_name, "First picture category didn't open"

    # 6) Открыть 1 картинку , проверить что открылась
    def open_first_picture_and_check(self):
        global first_pic_url
        first_pic = self.browser.find_element(*PictPageLocators.FIRST_PICTURE)
        first_pic_url = first_pic.get_attribute("href")
        lst = first_pic_url.split("&")
        for part in lst:
            if "img_url" in part:
                first_pic_url = part
        first_pic.click()
        time.sleep(1)
        current_url = self.browser.current_url
        assert first_pic_url in current_url, "First picture didn't open"
        
        # 7) При нажатии кнопки вперед  картинка изменяется
    def click_next_picture_button(self):
        self.browser.find_element(*PictPageLocators.NEXT_BUTTON).click()

    # 8) При нажатии кнопки назад картинка изменяется на изображение из шага 6. 
    # Необходимо проверить, что это то же изображение.
    def click_previous_picture_button(self):
        self.browser.find_element(*PictPageLocators.PREVIOUS_BUTTON).click()
        time.sleep(1)
        current_url = self.browser.current_url
        print(first_pic_url)
        print(current_url)
        assert first_pic_url in current_url, "First picture didn't reopen"