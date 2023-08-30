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
    def test_TC_SignUp(self):  # Negative Test Case
        try:
            SignUpBtn = HomePage(self.driver)
            WebDriverWait(self.driver, 10000).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[@class='signUp'])[2]")))

            if SignUpBtn.ClickSignUp().click():
                print("SignUp is Clickable")

            SignUp = SignupPage(self.driver)
            WebDriverWait(self.driver, 10000).until(
                EC.element_to_be_clickable((By.XPATH, "(//a[@class='signUp'])[2]")))
            SignUp.Wait("//input[@id='email']")
            SignUp.EnterEmail().send_keys("InvalidEmail")
            Email_Error = str(SignUp.ReadEmailError().text)
            if Email_Error == "Please enter a valid email address":
                print("Email Negative test is is success")

            SignUp.Wait("//input[@id='password']")
            SignUp.EnterPassword().send_keys("Pasword")
            Password_Error = str(SignUp.ReadPasswordError().text)
            if Password_Error == "Password cannot be less than 8 characters":
                print("Password Negative test is is success")
                # "Password should not contain continuous characters"

            SignUp.Wait("//input[@id='rmobile']")
            SignUp.EnterMobileNumber().send_keys("12345678")
            Number_Error = str(SignUp.ReadNumberError().text)
            if Number_Error == "Please enter a valid mobile number.":
                print("Number Negative test is is success")

            CheckBox_Error = str(SignUp.CheckBoxErrorMessage.text)
            if CheckBox_Error == "Please read and accept the Terms of Service and Privacy Policy":
                print("CheckBox Negative test is is success")

            SignUp.Wait("//input[@id='signupbtn']")
            if SignUp.ClickSignin().click():
                print("Submit Button is Clickable")
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")
