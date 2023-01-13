import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1900, 1080")
    options.add_argument("--no-sandbox")
    # для работы в докер контейнере
    # driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", chrome_options=options)
    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

