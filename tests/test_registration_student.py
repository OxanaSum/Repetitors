import random
import time

from selenium.webdriver.common.by import By
from data.urls import Urls
import selenium
from data import credentials
from locators.registration_page_locators import RegistrationPageLocators as reg_loc
from locators.student_account_page_locators import StudentAccountPageLocators as stud_loc

def test_visit(driver):
    button_registration_locator = "//a[text()='Регистрация']"

    login_for_registration = "Oksana" + str(random.randint(0, 99))
    password_for_registration = "bklmd246%" + str(random.randint(0, 99))

    driver.get(Urls.repetitor_main_url)
    driver.find_element(By.XPATH,button_registration_locator).click()
    driver.find_element(By.XPATH, reg_loc.fild_login_locator).send_keys(login_for_registration)
    driver.find_element(By.XPATH, reg_loc.fild_password_locator).send_keys(password_for_registration)
    driver.find_element(By.XPATH, reg_loc.fild_pass_confirm_locator).send_keys(password_for_registration)
    driver.find_element(By.XPATH, reg_loc.button_submit_locator).click()
    text = driver.find_element(By.XPATH, stud_loc.success_registration_locator).text

    assert text == "Вы успешно зарегистрировались!"

