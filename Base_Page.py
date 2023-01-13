from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        try:
            self.driver = driver
            self.base_url = "https://kitaphane.tatarstan.ru"
        except IOError as e:
            print(e)

    # Поиск определённого элемента
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # Поиск всех возможных элементов
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # Запуск сайта
    def go_to_site(self):
        return self.driver.get(self.base_url)

    def check_exists_by_css_selector(self, css_locator):
        try:
            self.find_element(css_locator)
        except TimeoutException:
            return False
        return True

    # Сравнение значений по листу
    def check_str_val_in_str_list(self, list_1, val):
        if not list_1:
            return False
        # traverse in the list
        for x in list_1:

            # compare with all the values
            # with val
            if val not in x:
                return False
        return True
