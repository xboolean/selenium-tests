from datetime import datetime
import csv

from selenium.webdriver.common.by import By


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def write_to_csv(rows):
    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) == 3:
            if cells[0].text:
                date_time = cells[0].text
                dt = datetime.strptime(date_time, "%b %d, %Y %I:%M:%S %p")
                formatted_date_time = dt.strftime("%d:%m:%Y %H:%M:%S")
                amount = cells[1].text
                transaction_type = cells[2].text
                data.append((formatted_date_time, amount, transaction_type))
    csv_file = "transactions.csv"

    with open(csv_file, mode="w") as file:
        writer = csv.writer(file)
        writer.writerow(["Дата-времяТранзакции", "Сумма", "ТипТранзакции"])
        writer.writerows(data)
    return csv_file
