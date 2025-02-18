# 1. Чтение файла и извлечение номера чека
import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()


match = re.search(r"Чек №(\d+)", text)
if match:
    receipt_number = match.group(1)
    print("Номер чека:", receipt_number)

#---------------------------------------------------------------
# 2. Извлечение списка товаров
import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()


pattern = r"(\d+\.)\n(.+)\n([\d,]+) x ([\d,]+)\n([\d,]+)"
matches = re.findall(pattern, text)

for match in matches:
    item_number = match[0].strip()
    item_name = match[1].strip()
    quantity = match[2].replace(",", ".")
    price_per_unit = match[3].replace(",", ".")
    total_price = match[4].replace(",", ".")
    
    print(f"Товар {item_number}: {item_name}")
    print(f"Количество: {quantity}, Цена за единицу: {price_per_unit}, Общая стоимость: {total_price}")
    print("-" * 40)

#---------------------------------------------------------------
# 3. Извлечение общей суммы
import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()


match = re.search(r"ИТОГО:\n([\d\s,]+)", text)
if match:
    total_amount = match.group(1).replace(" ", "").replace(",", ".")
    print("Общая сумма:", total_amount)

#---------------------------------------------------------------
# 4. Извлечение даты и времени
import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()


match = re.search(r"Время: (\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})", text)
if match:
    datetime = match.group(1)
    print("Дата и время:", datetime)

#---------------------------------------------------------------
# 5. Извлечение адреса
import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()


match = re.search(r"г\. (.+)", text)
if match:
    address = match.group(1)
    print("Адрес:", address)