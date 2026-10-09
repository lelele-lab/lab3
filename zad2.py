# Факториал n! (while)
n = int(input("Введите n: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"{n}! = {fact}")

#  Ряд 1 + 1/2! + ... + 1/n! (while)
summa = 0
current_fact = 1
i = 1
while i <= n:
    current_fact *= i
    summa += 1 / current_fact
    i += 1
print("Сумма ряда:", summa)