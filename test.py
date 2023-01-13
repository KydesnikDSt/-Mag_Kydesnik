from Main_Page import MainPageHelper
from Search_Result_Page import SearchPageHelper
from Document_Page import DocumentPageHelper
from ElectronCatalog_Page import ElectronCatalogPageHelper
from Mailing_Page import MailingPageHelper
import allure


@allure.step
def test_check_logo(browser):
    # Открытие браузера и запуск страницы сайта
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    # Проверяю наличие логотипа на странице сайта
    assert main_page.check_logo()


@allure.step
def test_site_search(browser):
    # Открытие браузера и запуск страницы сайта
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    # Открытие поисковой строки и ввод переменной, которую мы в дальнейшем будем искать в поисковой строке
    text_of_search = "Виртуальная выставка"
    main_page.search_in_site(browser, text_of_search)
    # Переход на страницу поисковой строки и результатов поиска
    search_result_page = SearchPageHelper(browser)
    # Проверка результатов поиска по сайту
    assert search_result_page.check_exist_text_in_list_results(browser, text_of_search)


@allure.step
def test_information_about_the_library(browser):
    # Открытие браузера и запуск страницы сайта
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    # Переходим к пункту меню страницы сайта 'О библиотеке'
    main_page.go_to_library_information()
    doc_page = DocumentPageHelper(browser)
    # Переходим по строке(ссылке) 'Документы', открываем её содержимое
    doc_page.go_to_documents(browser)
    assert doc_page.check_exist_document_on_page(browser)


@allure.step
def test_electron_catalog(browser):
    # Открытие браузера и запуск страницы сайта
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    # Нажимаем на кнопку 'Электронный каталог'
    main_page.string_of_electron_catalog()
    # Создаю переменные которые мы будем использовать в электронном каталоге
    name = "Есенин"
    material = "Сериальные"
    # Переходим на электронный каталог
    electron_catalog = ElectronCatalogPageHelper(browser)
    # Указываем необходимый тип нужного материала
    electron_catalog.reqired_materials(material)
    # Указываю поиск по фильтру 'Автор'
    electron_catalog.book_author(name)
    # Просматриваю список количества найденных результатов поиска, позже возвращаясь к каталогу
    electron_catalog.view_button(browser)
    # Запускаю поиск по указанным фильтрам и категориям
    electron_catalog.find_button()
    # Вывожу результат поиска по Электронному каталогу
    assert electron_catalog.result_of_search(browser)


@allure.step
def test_newsletter(browser):
    # Открытие браузера и запуск страницы сайта
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    # Открытие пункта меню страницы сайта 'Деятельность'
    main_page.open_toggle_for_activity()
    # Переход к пункту 'Рассылка новостей'
    main_page.go_to_newsletter()
    # Создание переменную для дальнейшего указания в строке указания e-mail
    email = "yandex.ru"
    mailing_page = MailingPageHelper(browser)
    # Создание динамического ожидания для прогрузки страницы Рассылки новостей
    mailing_page.input_text_email(browser, email)
    # Активация кнопки Подписаться
    mailing_page.subscribe_to_the_newsletter()
    # Вывод строки ошибки, из-за неверного ввода типа почты
    assert mailing_page.check_present_error_message()

