user_seconds = int(input("Введите количество секунд: "))
if user_seconds < 60:
    print(f"00:00:{user_seconds:02}")
elif user_seconds < 3600:
    print(f"00:{user_seconds // 60:02}:{user_seconds % 60:02}")
else:
    print(f"{user_seconds // 3600:02}:{user_seconds % 60:02}:{user_seconds % 60:02}")