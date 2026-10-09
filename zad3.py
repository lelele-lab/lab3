N = int(input("Введите N: "))

print(f"Простые числа от 2 до {N}:")

for num in range(2, N + 1):
    is_prime = True
    
    # Проверяем делители от 2 до корня из num
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break  # Нашли делитель — число не простое, выходим из while
        divisor += 1
        
    if not is_prime:
        continue  # Пропускаем вывод, если число составное
        
    print(num, end=" ")

print()