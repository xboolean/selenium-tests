from selenium.webdriver.common.by import By


class BankLocators:
    LOGIN = (By.XPATH, "//button[contains(text(), 'Customer Login')]")
    SELECT = (By.ID, "userSelect")
    AUTHORIZE = (By.XPATH, "//button[contains(text(), 'Login')]")
    AUTHORIZE_CHECK = (By.XPATH, "//span[contains(text(), 'Harry Potter')]")
    SELECT_VALUE = (By.XPATH, "//options[contains(text(), 'Harry Potter')]")
    DEPOSIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Deposit')]")
    TRANSACTION_INPUT = (By.XPATH, "//input[@type='number']")
    TRANSACTION_SUBMIT = (
        By.XPATH,
        "//button[@type='submit']",
    )
    WITHDRAWL = (By.XPATH, "//button[contains(text(), 'Withdrawl')]")
    TRANSACTION_INPUT = (By.XPATH, "//input[@type='number']")
    BALANCE = (By.XPATH, "//div[@class='center']/strong[@class='ng-binding'][2]")
    TRANSACTIONS = (By.XPATH, "//button[contains(text(), 'Transactions')]")
    TABLE = (By.XPATH, "//table[@class='table table-bordered table-striped']/tbody")
    TABLE_CSS = (By.CSS_SELECTOR, "table tbody tr")
    TABLE_TR = (By.XPATH, "//table/tbody/tr[2]/td")
    ROWS = (By.TAG_NAME, "tr")
    TABLE_RESET = (By.XPATH, "//button[@ng-click='reset()']")
