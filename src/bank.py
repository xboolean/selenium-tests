from time import sleep
from .base import BasePage
from .locators import BankLocators
from selenium.webdriver.common.by import By


class BankPageObject(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(
            "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        )

    def login(self, value):
        assert "XYZ Bank" in self.driver.title
        self.click(BankLocators.LOGIN)
        self.click(BankLocators.AUTHORIZE)

    def deposit(self, amount):
        self.click(BankLocators.DEPOSIT_BUTTON)
        self.find_element(BankLocators.TRANSACTION_INPUT).send_keys(amount)
        self.click(BankLocators.TRANSACTION_SUBMIT)

    def withdrawl(self, amount):
        self.click(BankLocators.WITHDRAWL)
        self.find_element(BankLocators.TRANSACTION_INPUT).send_keys(amount)
        self.click(BankLocators.TRANSACTION_SUBMIT)

    def check_balance(self):
        return self.find_element(BankLocators.BALANCE).text

    def transactions(self):
        self.driver.refresh()
        self.click(BankLocators.TRANSACTIONS)
        tbody = self.find_elements(BankLocators.TABLE_CSS)
        return tbody
