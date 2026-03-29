from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class FormPage:
    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)

    def _js_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def fill_name(self, name):
        self.driver.find_element(By.ID,"name-input").send_keys(name)
        return self

    def fill_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys(password)
        return self

    def select_drinks(self):
        self._js_click(self.driver.find_element(By.ID, "drink2")) # Milk
        self._js_click(self.driver.find_element(By.ID, "drink3")) # Coffee
        return self

    def select_color(self):
        self._js_click(self.driver.find_element(By.ID, "color3")) # Yellow
        return self

    def select_automation(self):
        select = Select(self.driver.find_element(By.ID, "automation"))
        select.select_by_value("yes")
        return self

    def fill_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)
        return self

    def fill_message(self, message):
        self.driver.find_element(By.ID, "message").send_keys(message)
        return self

    def submit_button(self):
        self._js_click(self.driver.find_element(By.ID, "submit-btn"))
        return self
