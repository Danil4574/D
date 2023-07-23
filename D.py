def check_password(input_password, stored_password):
    """
    Функция для проверки введенного пароля.

    Parameters:
        input_password (str): Введенный пользователем пароль.
        stored_password (str): Хешированный пароль, хранящийся на сервере.

    Returns:
        bool: True, если пароль верен, иначе False.
    """
    # В реальном приложении хранилище паролей должно использовать хеширование, например, с помощью bcrypt.
    # Здесь для примера сравним пароли напрямую.
    return input_password == stored_password


# Пример использования:
stored_password = "hash123"  # В реальном приложении здесь будет хеш пароля, а не сам пароль.
user_input = input("Введите пароль: ")

if check_password(user_input, stored_password):
    print("Пароль верен. Добро пожаловать!")
else:
    print("Неверный пароль. Попробуйте еще раз.")
