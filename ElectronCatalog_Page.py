from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Base_Page import BasePage


class ElectronCatalogPageLocators:
    LOCATOR_AUTHOR_BOOK = (By.CSS_SELECTOR, "body > form > input:nth-child(10)")
    LOCATOR_REQIRED_MATERIALS = (By.CSS_SELECTOR, "body > form > table:nth-child(7) > tbody > tr:nth-child(2) > "
                                                  "td:nth-child(1) > select")
    LOCATOR_FIND_BUTTON = (By.CSS_SELECTOR, "body > form > table:nth-child(22) > tbody > tr > td:nth-child(2) > "
                                            "input[type=submit]:nth-child(2)")
    LOCATOR_VIEW_BUTTON = (By.CSS_SELECTOR, "body > form > table:nth-child(22) > tbody > tr > td:nth-child(2) > "
                                            "input[type=submit]:nth-child(3)")
    LOCATOR_RESULTS_OF_VIEW = (By.CSS_SELECTOR, "body")
    LOCATOR_RETURN_IN_CATALOG = (By.CSS_SELECTOR, "body > div:nth-child(1) > a:nth-child(1)")
    LOCATOR_RESULT = (By.CSS_SELECTOR, "body")


class ElectronCatalogPageHelper(BasePage):

    def reqired_materials(self, material):
        # Забираем все типы материала(изданий)
        reqired_materials = self.find_elements(ElectronCatalogPageLocators.LOCATOR_REQIRED_MATERIALS)
        # Создаём цикл, где идёт поиск по конкретному материалу, а также выбираем его из списка
        for materials in reqired_materials:
            if material in materials.text:
                materials.click()

    def book_author(self, name):
        # Поиск строки записи элемента Автор, его активация
        book_author = self.find_element(ElectronCatalogPageLocators.LOCATOR_AUTHOR_BOOK)
        book_author.click()
        # Заполнение строки для поиска по автору в электронном каталоге
        name_author = self.find_element(ElectronCatalogPageLocators.LOCATOR_AUTHOR_BOOK)
        name_author.send_keys(name)

    def find_button(self):
        # Запускаю поиск по указанным категориям и фильтрам
        find_button = self.find_element(ElectronCatalogPageLocators.LOCATOR_FIND_BUTTON)
        find_button.click()

    def view_button(self, browser):
        # Переход к просмотру всех возможных результатов поиска после заполнения строки значение
        view_button = self.find_element(ElectronCatalogPageLocators.LOCATOR_VIEW_BUTTON)
        view_button.click()
        # Создаю динамическое ожидание списка результатов просмотра
        WebDriverWait(browser, 5).until(
            ec.visibility_of_all_elements_located(ElectronCatalogPageLocators.LOCATOR_RESULTS_OF_VIEW))
        # Задаю возвращение на форму запроса после просмотра всех возможных результатов поиска
        return_in_catalog = self.find_element(ElectronCatalogPageLocators.LOCATOR_RETURN_IN_CATALOG)
        return_in_catalog.click()

    def result_of_search(self, browser):
        # Создаю динамическое ожидание прогрузки страницы с результатами
        WebDriverWait(browser, 5).until(ec.visibility_of_element_located(ElectronCatalogPageLocators.LOCATOR_RESULT))
        result_of_search = self.find_element(ElectronCatalogPageLocators.LOCATOR_RESULT)
        # Возвращаю результат поиска
        return result_of_search
