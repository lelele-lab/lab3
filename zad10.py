import random  # подключаем модуль для случайных чисел

# Генерируем случайное число от 1 до 100
secret = random.randint(1, 100)

print("Угадай число от 1 до 100!")

popytki = 0  # счётчик попыток

# Крутим цикл, пока пользователь не угадает
while True:
    ugaday = int(input("Твоя догадка: "))
    popytki += 1  # увеличиваем счётчик
    
    if ugaday < secret:
        print("Больше!")
    elif ugaday > secret:
        print("Меньше!")
    else:
        print(f"Угадал за {popytki} попыток!")
        break  # выходим из цикла, когда число угадано