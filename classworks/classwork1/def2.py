# Заготовка и пример вызова:
def cat_speak(phrase, mood="обычный"):
    # Ваш код здесь
    if mood == 'голодный':
        adding='МЯУ! Покорми!'
    if mood == 'довольный':
        adding='мур-мур...'
    else:
        adding=0
    return f"{phrase} - {adding}"

print(cat_speak("Я проснулся", mood="голодный"))
# Ожидаемый результат: "Я проснулся — МЯУ! Покорми!"
