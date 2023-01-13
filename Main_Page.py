import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Base_Page import BasePage


class MainPageLocators:
    # Здесь будут находиться локаторы
    LOCATOR_MAIN_LOGO = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[1]/a")
    LOCATOR_SEARCH_BUTTON_LOUPE = (By.CSS_SELECTOR, "#app > div.header.headroom.headroom--top.headroom--not"
                                                    "-bottom > div > div.header__tools > div.hidden-xs > "
                                                    "div.header__search > div > form > span > span")
    LOCATOR_INPUT_TEXT_FOR_SEARCH = (By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div["
                                               "2]/div/form/div/input")
    LOCATOR_ABOUT_THE_LIBRARY = (By.CSS_SELECTOR, "#app > div.header.headroom.headroom--top.headroom--not-bottom > "
                                                  "div > div.header__menu.hidden-xs > div > div:nth-child(1)")
    LOCATOR_WAIT_DOWNLOAD_SITE = (By.CSS_SELECTOR, "#app")
    LOCATOR_ELECTRON_CATALOG_BUTTON = (By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div/div[4]/a")
    LOCATOR_ANOTHER_POSITION = (By.CSS_SELECTOR, "#app > div.header.headroom.headroom--top.headroom--not-bottom")
    LOCATOR_OPEN_TOGGLE_FOR_ACTIVITY = (By.CSS_SELECTOR, "#app > div.header.headroom.headroom--top.headroom--not"
                                                         "-bottom > div > div.header__menu.hidden-xs > div > "
                                                         "div:nth-child(2) > a")
    LOCATOR_GO_TO_NEWSLETTER = (By.CSS_SELECTOR, "#activity-block > div.activity > div:nth-child(3) > div:nth-child(2)")


class MainPageHelper(BasePage):

    def check_logo(self):
        # Создаём условие,которе будет искать логотип нашего сайта. При отсутствии логотипа будет выдаваться ошибка.
        try:
            logo = self.find_element(MainPageLocators.LOCATOR_MAIN_LOGO)
            return logo.is_displayed()
        except TimeoutException:
            return False

    def search_in_site(self, browser, text_of_search):
        # Создаём динамическое ожидание списка документов
        WebDriverWait(browser, 5).until(ec.visibility_of_element_located(MainPageLocators.LOCATOR_WAIT_DOWNLOAD_SITE))
        # Указываем поиск элемента Лупа(поисковик), для дальнейшей активации
        search_loupe = self.find_element(MainPageLocators.LOCATOR_SEARCH_BUTTON_LOUPE)
        search_loupe.click()
        # После активации поисковика по сайту, вводим значение переменной
        search_enter_text = self.find_element(MainPageLocators.LOCATOR_INPUT_TEXT_FOR_SEARCH)
        search_enter_text.send_keys(text_of_search)
        # Запускаем работу поисковика, с помощью клавиши ENTER
        search_enter_text.send_keys(Keys.ENTER)

    def open_toggle_for_activity(self):
        # Открытие пункта меню страницы сайта 'Деятельность'
        open_toggle_for_activity = self.find_element(MainPageLocators.LOCATOR_OPEN_TOGGLE_FOR_ACTIVITY)
        open_toggle_for_activity.click()

    def go_to_newsletter(self):
        # Переход к пункту 'Рассылка новостей'
        go_to_newsletter = self.find_element(MainPageLocators.LOCATOR_GO_TO_NEWSLETTER)
        go_to_newsletter.click()

    def go_to_library_information(self):
        # Переход к пункту страницы 'О библиотеке'
        transition_to_information = self.find_element(MainPageLocators.LOCATOR_ABOUT_THE_LIBRARY)
        transition_to_information.click()

    def string_of_electron_catalog(self):
        # Кликаем по строке(ссылке) Электронный каталог
        string_of_electron_catalog = self.find_element(MainPageLocators.LOCATOR_ELECTRON_CATALOG_BUTTON)
        string_of_electron_catalog.click()
