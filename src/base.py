from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def select(self, locator, value, time=20):
        # select = Select(self.find_element((By.ID, "userSelect")))
        select = Select(self.find_element(locator))
        return select.select_by_value("2")

    def select_by_xpath(self, locator, value, time=20):
        return self.find_element(
            (By.XPATH, '//select[@name="userSelect"]/option[@value="2"]')
        ).click()

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)
        ).click()
