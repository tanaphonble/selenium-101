import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        driver_service = Service(
            executable_path="../chromedriver")
        driver = webdriver.Chrome(
            service=driver_service, options=chrome_options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.example.com/login")
        driver.execute_script("window.localStorage.setItem('accessToken', 'whitelist')")
        driver.get("https://www.example.com")

    elif browser_name == "firefox":
        print("not implemented")
        exit

    request.cls.base_driver = driver
    yield
    time.sleep(1)
    driver.close()
