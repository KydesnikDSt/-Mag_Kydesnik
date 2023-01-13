import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Base_Page import BasePage


class DocumentPageLocators:
    LOCATOR_DOCUMENTS = (By.CSS_SELECTOR, "#wysiwyg > div > gl-dirty-html > div:nth-child(3) > a")
    LOCATOR_DOCUMENTS_RESULTS = (By.CSS_SELECTOR, "#app > div.content.index-menu-container > div.container-fluid > "
                                                  "div > div.content__main.col-xs-12.col-sm-8")
    LOCATOR_LINK_TO_SPECIFIC_DOCUMENTS = (By.CSS_SELECTOR, "#wysiwyg > div > gl-dirty-html > ul > li")


class DocumentPageHelper(BasePage):

    def go_to_documents(self, browser):
        # Создаём динамическое ожидание визуального подтверждения видимости строки 'Документы'
        WebDriverWait(browser, 5).until(ec.visibility_of_element_located(DocumentPageLocators.LOCATOR_DOCUMENTS))
        # Поиск строки(ссылки) 'Документы' и переход по ней(её открытие)
        go_to_documents = self.find_element(DocumentPageLocators.LOCATOR_DOCUMENTS)
        return go_to_documents.click()

    def check_exist_document_on_page(self, browser):
        # Создаём динамическое ожидание списка документов
        WebDriverWait(browser, 5).until(
            ec.visibility_of_element_located(DocumentPageLocators.LOCATOR_DOCUMENTS_RESULTS))
        check_text = self.find_elements(DocumentPageLocators.LOCATOR_LINK_TO_SPECIFIC_DOCUMENTS)
        size_list_elements = len(check_text)
        # Выбираем случайный индекс в пределах длины списка
        item = random.randint(1, size_list_elements - 1)
        # Возврат случайного индекса
        return check_text[item].is_displayed()
