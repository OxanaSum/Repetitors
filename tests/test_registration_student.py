import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import conftest

def test_visit(driver):
    driver.get("http://195.133.27.184")
    time.sleep(2)