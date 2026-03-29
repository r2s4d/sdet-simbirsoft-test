from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class FormPage:
    URL = "https://practice-automation.com/form-fields/"

    # Локаторы — Page Factory
    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    DRINK_MILK = (By.ID, "drink2")
    DRINK_COFFEE = (By.ID, "drink3")
    COLOR_YELLOW = (By.ID, "color3")
    AUTOMATION_SELECT = (By.ID, "automation")
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_INPUT = (By.ID, "message")
    SUBMIT_BTN = (By.ID, "submit-btn")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)

    def _js_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def fill_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        return self

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        return self

    def select_drinks(self):
        self._js_click(self.driver.find_element(*self.DRINK_MILK))
        self._js_click(self.driver.find_element(*self.DRINK_COFFEE))
        return self

    def select_color(self):
        self._js_click(self.driver.find_element(*self.COLOR_YELLOW))
        return self

    def select_automation(self):
        select = Select(self.driver.find_element(*self.AUTOMATION_SELECT))
        select.select_by_value("yes")
        return self

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        return self

    def fill_message(self, message):
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)
        return self

    def submit_button(self):
        self._js_click(self.driver.find_element(*self.SUBMIT_BTN))
        return self
