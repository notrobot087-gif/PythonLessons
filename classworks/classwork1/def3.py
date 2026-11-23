# Заготовка и пример вызова:
def total_score(*points, bonus=0):
    # Ваш код здесь
    total = sum(points) + bonus
    if total <=0:
        total = 0
        
    return total

print(total_score(10, -15, 20, bonus=5))   # Ожидается: 20
print(total_score(5, -20, bonus=0))       # Ожидается: 0

