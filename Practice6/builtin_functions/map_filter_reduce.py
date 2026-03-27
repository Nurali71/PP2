from functools import reduce

# Наш список данных
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. MAP: Возводим каждое число в квадрат
# map(функция, список)
squared = list(map(lambda x: x**2, numbers))
print(f"Квадраты: {squared}")

# 2. FILTER: Оставляем только четные числа
# filter(условие, список)
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Только четные: {evens}")

# 3. REDUCE: Перемножаем все числа между собой  (1*2*3...)
# Сначала нужно импортировать из functools
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"Произведение 1-5: {product}")