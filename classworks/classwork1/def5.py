# Данные и пример вызова:
movies = [
    {"title": "Начало", "genre": "фантастика"},
    {"title": "Один дома", "genre": "комедия"},
    {"title": "Интерстеллар", "genre": "фантастика"},
]

def pick_movie(movies, genre):
    # Ваш код здесь
    rated_movies = []
    for movie in movies:
        if movie["genre"] == genre:
            rated_movies.append(movie["title"])
    return rated_movies

print(pick_movie(movies, "фантастика"))
