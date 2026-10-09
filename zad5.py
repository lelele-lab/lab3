#  Первые n чисел Фибоначчи
n = int(input("Сколько чисел Фибоначчи вывести: "))

a, b = 0, 1
fibs = []
i = 0
while i < n:
    fibs.append(a)
    a, b = b, a + b
    i += 1

print("Ряд:", fibs)

# Проверка принадлежности
x = int(input("Какое число проверить: "))

if x in fibs:
    print(f"{x} принадлежит ряду")
else:
    print(f"{x} НЕ принадлежит ряду")