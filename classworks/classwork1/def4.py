# Заготовка и пример вызова:
def check_password(password):
    # Ваш код здесь
    if len(password) < 6 or password.isdigit()==True:
        return ('Слабый')
    if len(password) > 6 or password.isdigit()==False:
        return('Нормальный')

print(check_password("1234567"))  # Ожидается: "Слабый"
print(check_password("kot2026"))  # Ожидается: "Нормальный"
