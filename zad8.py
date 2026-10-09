n = int(input("Введите число: "))

print("Делители числа", n, ":")

delitel = 1       # начинаем с 1
summa = 0         # сумма делителей

while delitel < n:
    if n % delitel == 0:     # если делится без остатка
        print(delitel, end=" ")
        summa += delitel     # добавляем к сумме
    delitel += 1

print()
print("Сумма делителей:", summa)

# Проверка на совершенное число
if summa == n:
    print(n, "— совершенное число!")
else:
    print(n, "— НЕ совершенное число")