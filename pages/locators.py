from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_BOX = (By.CSS_SELECTOR, "input#text")
    SUGGESTS_TABLE = (By.CSS_SELECTOR, "div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile.mini-suggest__popup_visible")
    SEARCH_RESULTS = (By.XPATH, '//*[@id="search-result"]/li/div/div[1]/div[1]/a/b')

class PictPageLocators():
    PICTURES_LINK = (By.XPATH, "//li[3]/a/div[1]")
    FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    FIRST_CATEGORY_NAME = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
    SEARCH_BOX_UNIQ = (By.CSS_SELECTOR, "input.input__control")
    # FIRST_PICTURE = (By.CLASS_NAME, "serp-item_pos_0")
    FIRST_PICTURE = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a")
    NEXT_BUTTON = (By.CSS_SELECTOR, "div.CircleButton.CircleButton_type_next")
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, "div.CircleButton_type_prev")
