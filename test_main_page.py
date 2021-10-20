from .pages.main_page import MainPage
from .pages.pict_page import PictPage
import pytest

def test_is_tensor_ru_in_top_five_search_results(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.is_tensor_ru_in_top_five_search_results()

def test_does_pictures_page_work(browser):
    link = "https://yandex.ru/"
    page = PictPage(browser, link)
    page.does_pictures_page_work()