import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# @pytest.fixture
# def driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--profile-directory=Default")
#     chrome_options.add_argument("--user-data-dir=~/.config/google-chrome")
#     driver = webdriver.Chrome(options=chrome_options)
#     yield driver
#     driver.delete_all_cookies()
#     driver.quit()


# Selenium Grid Driver


@pytest.fixture
def remote_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Remote(
        options=options,
        command_executor="http://selenium-chrome:4444",
    )
    yield driver
    driver.delete_all_cookies()
    driver.quit()
