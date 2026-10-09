M = int(input("Введите M: "))

print(f"Таблица степеней двойки до первой > {M}:")

power = 0
value = 1

while True:
    print(f"2^{power} = {value}")
    
    if value > M:
        break  # Нашли первое число больше M, выходим
    
    power += 1
    value *= 2  # Умножаем на 2 для следующей степени