import allure
import pytest
from pages.form_page import FormPage

def test_form_submission(driver):
    page = FormPage(driver)
    (
        page
        .fill_name("Egor")
        .fill_password("12345")
        .select_drinks()
        .select_color()
        .select_automation()
        .fill_email("egor@example.com")
        .fill_message("5, Katalon Studio")
        .submit_button()
    )
    alert = driver.switch_to.alert
    assert alert.text == "Message received!"
