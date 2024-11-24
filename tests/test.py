from data.urls import Urls

class TestFirstTry:
    url = Urls()

    def test_open_url(self, driver):
        driver.get(Urls.repetitor_main_url)