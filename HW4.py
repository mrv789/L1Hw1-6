user_number = int(input('Ведите целое положительное число: '))
max_number = 0
while user_number > 0:
    if user_number % 10 > max_number:
        max_number = user_number % 10
        if max_number == 9:
            break
    user_number //= 10

print(f"Наибольшая цифра числа: {max_number}")