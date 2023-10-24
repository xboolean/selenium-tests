import time
import datetime

import allure
import pytest

from src.bank import BankPageObject
from src.locators import BankLocators
from src.utils import fibonacci, write_to_csv


@allure.story("Тестирование сайта globalsqa и выгрузка csv")
def test_bank_site(remote_driver):
    site = BankPageObject(remote_driver)

    with allure.step("Авторизация"):
        site.login(BankLocators.SELECT_VALUE)
        assert "Harry Potter" in site.find_element(BankLocators.AUTHORIZE_CHECK).text

    fibonacci_number = fibonacci(datetime.datetime.now().day + 1)

    with allure.step("Пополнение счета"):
        site.deposit(fibonacci_number)
        site.check_balance() == fibonacci_number

    with allure.step("Списание со счета"):
        site.withdrawl(fibonacci_number)

    with allure.step("Проверка, что баланс не изменился"):
        site.check_balance() == 0

    with allure.step("Переход на страницу с транзакциями"):
        table_rows = site.transactions()
        assert len(table_rows) == 2

    allure.attach.file(
        write_to_csv(table_rows), attachment_type=allure.attachment_type.CSV
    )

    site.click(BankLocators.TABLE_RESET)


def test_remote_driver(remote_driver):
    remote_driver.get("https://google.com")
    assert "Google" in remote_driver.title
