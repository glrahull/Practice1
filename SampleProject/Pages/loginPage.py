from selenium.webdriver.common.by import By
from SampleProject.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        username_testbox_name = Locators.username_testbox_name
        password_textbox_name = Locators.password_textbox_name
        login_button_xpath = Locators.login_button_xpath
        invalidUsername_message_xpath = Locators.invalidUsername_message_xpath

    def enter_username(self, username):
        self.driver.find_element(by=By.NAME, value=Locators.username_testbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(by=By.NAME, value=Locators.password_textbox_name).clear()
        self.driver.find_element(by=By.NAME, value=Locators.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(by=By.XPATH, value=Locators.login_button_xpath).click()

    def check_invalid_username_message(self, message):
        msg = self.driver.find_element(by=By.XPATH,value=Locators.invalidUsername_message_xpath).text
        return msg



