from selenium.webdriver.ie.webdriver import WebDriver

class BasePage:

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

