from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    ZohoIcon = (By.XPATH, "//a[normalize-space()='Zoho.com']")
    Password = (By.NAME, "password")
    SignUp = (By.XPATH, "(//a[@class='signUp'])[2]")

    def Wait(self,text):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(text))

    def ClickIcon(self):
        return self.driver.find_element(*HomePage.ZohoIcon)

    def ClickSignUp(self):
        return self.driver.find_element(*HomePage.SignUp)
