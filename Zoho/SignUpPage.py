from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    Email = (By.XPATH, "//input[@id='email']")
    Password = (By.XPATH, "//input[@id='password']")
    Mobile = (By.XPATH, "//input[@id='rmobile']")
    Submit = (By.XPATH, "//input[@id='signupbtn']")
    Checkbox = (By.XPATH, "//span[@id='signup-termservice']")
    CheckBoxErrorMessage = (By.XPATH, "//span[@id='signup-termservice']")
    EmailError = (By.XPATH, "//span[@id='email-error']")
    PasswordError = (By.XPATH, "//span[@id='password-error']")
    NumberError = (By.XPATH, "//span[@id='rmobile-error']")



    def EnterEmail(self):
        return self.driver.find_element(*SignupPage.Email)

    def EnterPassword(self):
        return self.driver.find_element(*SignupPage.Password)

    def EnterMobileNumber(self):
        return self.driver.find_element(*SignupPage.Mobile)

    def ClickCheckBox(self):
        return self.driver.find_element(*SignupPage.Checkbox)

    def ClickSignin(self):
        return self.driver.find_element(*SignupPage.Submit)

    def ReadCheckboxError(self):
        return self.driver.find_element(*SignupPage.CheckBoxErrorMessage)

    def ReadEmailError(self):
        return self.driver.find_element(*SignupPage.EmailError)

    def ReadPasswordError(self):
        return self.driver.find_element(*SignupPage.PasswordError)

    def ReadNumberError(self):
        return self.driver.find_element(*SignupPage.NumberError)

    def Wait(self,text):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(text))