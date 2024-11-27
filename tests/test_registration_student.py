import time
from selenium.webdriver.common.by import By
from data.urls import Urls
import selenium
from data import credentials
from locators.registration_page_locators import RegistrationPageLocators as loc

def test_visit(driver):
    button_registration_locator = "//a[text()='Регистрация']"

    login_for_registration = "Oksana"
    password_for_registration = "Oksana246%"

    driver.get(Urls.repetitor_main_url)
    driver.find_element(By.XPATH,button_registration_locator).click()
    time.sleep(2)
    driver.find_element(By.XPATH, loc.fild_login_locator).send_keys(login_for_registration)
    time.sleep(2)
    driver.find_element(By.XPATH, loc.fild_password_locator).send_keys(password_for_registration)
    time.sleep(2)
    driver.find_element(By.XPATH, loc.check_box_locator).click()
    time.sleep(2)
    driver.find_element(By.XPATH, loc.button_submit_locator).click()
    time.sleep(2)

    #assert

