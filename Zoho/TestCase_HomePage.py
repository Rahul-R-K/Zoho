import pytest
from HomePage import HomePage
import pytest
from SignUpPage import SignupPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class Testcase_Login:
    def test_TC_ZohoIcon_01(self):
        try:
            Icon = HomePage(self.driver)
            Icon.Wait("//a[normalize-space()='Zoho.com']")
            if Icon.ClickIcon().click():
                print("Icon is Clickable")
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")

    def test_TC_SignUp(self):  # Negative Test Case
        try:
            SignUpBtn = HomePage(self.driver)
            SignUpBtn.Wait("(//a[@class='signUp'])[2]")
            if SignUpBtn.ClickSignUp().click():
                print("SignUp is Clickable")
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")

        try:
            SignUp = SignupPage(self.driver)
            SignUp.Wait("//input[@id='email']")
            SignUp.EnterEmail().send_keys("InvalidEmail")
            Email_Error = str(SignUp.ReadEmailError().text)
            if Email_Error == "Please enter a valid email address":
                print("Negative test is is success")
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")

        try:
            SignUp = SignupPage(self.driver)
            SignUp.Wait("//input[@id='password']")
            SignUp.EnterPassword().send_keys("Pasword")
            Password_Error = str(SignUp.ReadPasswordError().text)
            if Password_Error == "Password cannot be less than 8 characters":
                print("Negative test is is success")
                # "Password should not contain continuous characters"
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")

        try:
            SignUp = SignupPage(self.driver)
            SignUp.Wait("//input[@id='rmobile']")
            SignUp.EnterMobileNumber().send_keys("12345678")
            Number_Error = str(SignUp.ReadNumberError().text)
            if Number_Error == "Please enter a valid mobile number.":
                print("Negative test is is success")
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")

        try:
            SignUp = SignupPage(self.driver)
            SignUp.Wait("//input[@id='signupbtn']")
            SignUp.ClickSignin().click()
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")
