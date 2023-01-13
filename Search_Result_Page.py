from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Base_Page import BasePage


class SearchPageLocators:
    LOCATOR_LIST_RESULTS = (By.CSS_SELECTOR, "#app > div.content > div.container-fluid > div.content__main > "
                                             "div.search_results > div > div > div.tabs__panels > div > div > div > "
                                             "div > div > div > div > div > h2")


class SearchPageHelper(BasePage):

    def check_exist_text_in_list_results(self, browser, text_of_search):
        # Создаём динамическое ожидание списка результатов поиска
        WebDriverWait(browser, 5).until(ec.visibility_of_element_located(SearchPageLocators.LOCATOR_LIST_RESULTS))
        list_results = self.find_elements(SearchPageLocators.LOCATOR_LIST_RESULTS)
        # Задаём цикл поиска переменной среди списка строк результатов
        for line in list_results:
            if text_of_search in line.text:
                return True
        return False
