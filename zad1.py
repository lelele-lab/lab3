#  Таблица умножения (вложенные for)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:4}", end="")
    print()

#  Сумма цифр (while + break для выхода)
num = int(input("\nВведите число (0 для выхода): "))
if num == 0:
    pass# break здесь не нужен, так как это не цикл, но логика простая
else:
    s = 0
    temp = abs(num) # берем модуль, чтобы работать с положительным
    while temp > 0:
        s += temp % 10
        temp //= 10
    print("Сумма цифр:", s)