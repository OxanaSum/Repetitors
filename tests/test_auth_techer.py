from selenium.webdriver.common.by import By
from data.urls import Urls
from locators.auth_page_locs import AuthorizationPageLocators as auth_loc
from data.credentials import Credentials as creds
from locators.teacher_account_page_locators import TeacherAccountPageLocators as teach_locs

def test_auth_teacher(driver):
    driver.get(Urls.auth_page_url)

    driver.find_element(By.CSS_SELECTOR, auth_loc.INPUT_AUTH_LOGIN).send_keys(creds.auth_login_teacher)
    driver.find_element(By.CSS_SELECTOR, auth_loc.INPUT_AUTH_PASSWORD).send_keys(creds.auth_password_teacher)
    driver.find_element(By.CSS_SELECTOR, auth_loc.BTN_SUBMIT).click()

    btn_create_listing = driver.find_element(By.XPATH, teach_locs.BTN_CREATE_LISTING)

    assert btn_create_listing.is_displayed()

