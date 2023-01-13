from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Base_Page import BasePage


class MailingPageLocators:
    LOCATOR_INPUT_TEXT_EMAIL_IN_PAGE = (By.CSS_SELECTOR, "#app > div.content.index-menu-container > "
                                                         "div.container-fluid > div")
    LOCATOR_INPUT_TEXT_EMAIL = (By.CSS_SELECTOR, "#email")
    LOCATOR_SUBSCRIBE_TO_NEWSLETTER_BUTTON = (By.CSS_SELECTOR, "#submit_btn")
    LOCATOR_ERROR = (By.CSS_SELECTOR, "#dnform > div > div")


class MailingPageHelper(BasePage):

    def input_text_email(self, browser, email):
        # Создание динамического ожидания для прогрузки страницы Рассылки новостей
        WebDriverWait(browser, 5).until(
            ec.visibility_of_element_located(MailingPageLocators.LOCATOR_INPUT_TEXT_EMAIL_IN_PAGE))
        input_text_email = self.find_element(MailingPageLocators.LOCATOR_INPUT_TEXT_EMAIL)
        input_text_email.click()
        input_text_email.send_keys(email)

    def subscribe_to_the_newsletter(self):
        # Активация кнопки ПОДПИСАТЬСЯ
        subscribe_to_the_newsletter = self.find_element(MailingPageLocators.LOCATOR_SUBSCRIBE_TO_NEWSLETTER_BUTTON)
        subscribe_to_the_newsletter.click()

    def check_present_error_message(self):
        return self.check_exists_by_css_selector(MailingPageLocators.LOCATOR_ERROR)
