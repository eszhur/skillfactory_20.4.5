import json
from collections import defaultdict
from datetime import datetime


# Чтение данных из файла JSON
file_path = r'C:\Users\Lenovo\Desktop\json\orders_july_23.json.txt'
with open(file_path, 'r') as file:
    data = json.load(file)

# Инициализация необходимых переменных
max_price_order_number = None
max_price = -1
max_quantity_order_number = None
max_quantity = -1
date_order_counts = defaultdict(int)
user_order_counts = defaultdict(int)
user_total_price = defaultdict(int)

total_orders = 0
total_price = 0
total_quantity = 0

# Обработка данных
for order_number, details in data.items():
    # Разбор данных заказа
    order_date = datetime.strptime(details['date'], '%Y-%d-%m')
    quantity = details['quantity']
    price = details['price']

    # 1. Номер самого дорогого заказа
    if price > max_price:
        max_price = price
        max_price_order_number = order_number

    # 2. Номер заказа с самым большим количеством товаров
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order_number = order_number

    # 3. Определение дня с наибольшим количеством заказов
    if order_date.month == 7 and order_date.year == 2023:
        date_order_counts[order_date.day] += 1

    # 4 и 5: Подсчет заказов и стоимости по пользователям
    user_id = details['user_id']
    user_order_counts[user_id] += 1
    user_total_price[user_id] += price

    # Общие показатели
    total_orders += 1
    total_price += price
    total_quantity += quantity

# 3. День с наибольшим количеством заказов
max_orders_day = max(date_order_counts, key=date_order_counts.get)

# 4. Пользователь с самым большим количеством заказов
top_user_by_orders = max(user_order_counts, key=user_order_counts.get)

# 5. Пользователь с самой большой суммарной стоимостью заказов
top_user_by_total_price = max(user_total_price, key=user_total_price.get)

# 6. Средняя стоимость заказа
if total_orders > 0:
    average_order_price = total_price / total_orders
else:
    average_order_price = 0

# 7. Средняя стоимость товаров
if total_quantity > 0:
    average_price_per_item = total_price / total_quantity
else:
    average_price_per_item = 0

# Вывод результатов
print(f"1. Номер самого дорогого заказа: {max_price_order_number}")
print(f"2. Номер заказа с самым большим количеством товаров: {max_quantity_order_number}")
print(f"3. День с наибольшим количеством заказов в июле: {max_orders_day}")
print(f"4. Пользователь с самым большим количеством заказов: {top_user_by_orders}")
print(f"5. Пользователь с самой большой суммарной стоимостью заказов: {top_user_by_total_price}")
print(f"6. Средняя стоимость заказа: {average_order_price:.2f}")
print(f"7. Средняя стоимость товара: {average_price_per_item:.2f}")