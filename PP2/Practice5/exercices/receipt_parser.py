# 1
import re

# Наш текст из чека
item_text = """
1.
Натрия хлорид 0,9%, 200 мл, фл
2,000 x 154,00
308,00
"""

# Паттерн:
# (\d+\.) — номер позиции (1.)
# \n(.*?)\n — захватываем название товара (все до следующей строки)
# (\d+,\d+)\s+x\s+(\d+,\d+) — количество (2,000) и цена за единицу (154,00)
# \n(\d+,\d+) — итоговая сумма за этот товар (308,00)
item_pattern = r"(\d+\.)\n(.*?)\n(\d+,\d+)\s+x\s+(\d+,\d+)\n(\d+,\d+)"

match = re.search(item_pattern, item_text, re.DOTALL)

if match:
    product = {
        "id": match.group(1),
        "name": match.group(2).strip(),
        "quantity": match.group(3),
        "unit_price": match.group(4),
        "total": match.group(5)
    }
    print(product)