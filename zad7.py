n = int(input("Введите число: "))
original = n          # сохраняем оригинал для сравнения
reversed_n = 0        # сюда будем собирать перевёрнутое число

temp = abs(n)         # работаем с положительным (минус не мешал)

while temp > 0:
    digit = temp % 10        # берём последнюю цифру
    reversed_n = reversed_n * 10 + digit  # "приписываем" её справа
    temp //= 10              # убираем последнюю цифру

print("В обратном порядке:", reversed_n)

# Проверка на палиндром
if original == reversed_n:
    print("Это палиндром!")
else:
    print("Не палиндром")