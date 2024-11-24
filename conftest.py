import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver


# @pytest.fixture(scope="session")
# def driver():
#     service = Service(executable_path=ChromeDriverManager().install())
#     options = webdriver.ChromeOptions()
#     options.add_argument("--window-size=1600,1000")
#     # options.add_argument("--headless")
#     # options.add_argument("--incognito")
#     # options.add_argument("--disable-cache")
#     # options.add_argument("--start-maximized")
#     # options.add_argument("--ignore-certificate-errors")
#     # options.page_load_strategy = "normal"
#     # options.page_load_strategy = "eager"
#     # options.page_load_strategy = "none"
#     driver = webdriver.Chrome(service=service, options=options)
#     # driver.set_window_size(1600, 900)
#     # driver.maximize_window()
#     yield driver
#     driver.quit()