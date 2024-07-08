import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import sys
import os

sys.path.append((os.path.join(os.path.dirname(__file__), "..", "..")))
from SampleProject.Pages.homePage import HomePage
from SampleProject.Pages.loginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_profile()
        homepage.click_logout()

        time.sleep(5)

    def test_02_login_invalid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element(by=By.XPATH, value="invalidUsername_message_xpath").text
        self.assertEquals(message, "Invalid credentials123")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:/Users/rahul/PycharmProjects/PageObjectModel/SampleProject/Reports"))
