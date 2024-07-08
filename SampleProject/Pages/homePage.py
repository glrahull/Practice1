from selenium.webdriver.common.by import By
from SampleProject.Locators.locators import Locators
class HomePage():


    def __init__(self,driver):
        self.driver = driver

        profile_link_xpath = Locators.profile_link_xpath
        logout_link_linkText = Locators.logout_link_linkText

    def click_profile(self):
        self.driver.find_element(By.XPATH,value=Locators.profile_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,value=Locators.logout_link_linkText).click()