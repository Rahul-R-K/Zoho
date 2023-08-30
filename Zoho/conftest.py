import time
import pytest as pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    s_obj = Service(executable_path="D:\Rahul Files\C Files\PycharmProjects\Demo\msedgedriver.exe")
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=s_obj, options=options)
    try:
        driver.get("https://www.zoho.com/")
        driver.maximize_window()
    except:
        print("WebPage is Not Working")
    request.cls.driver = driver
    yield
    time.sleep(10)
    driver.close()

