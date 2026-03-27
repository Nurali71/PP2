names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# 1. ENUMERATE: Когда нужен и индекс, и значение
print("Список студентов:")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# 2. ZIP: Склеиваем два списка в один (как застежка-молния)
print("\nРезультаты экзамена:")
combined = zip(names, scores)
for name, score in combined:
    print(f"{name} получил {score} баллов")

# 3. ALL и ANY: Быстрые проверки
grades = [True, True, False, True]
print(f"\nВсе сдали? {all(grades)}") # True если ВСЕ True
print(f"Хоть кто-то сдал? {any(grades)}") # True если хотя бы один True