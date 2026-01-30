import requests

# Публичное API JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/posts"

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем, что запрос успешен
response.raise_for_status()

# Превращаем ответ JSON в Python-список словарей
posts = response.json()

# Выводим заголовок и текст первых 5 постов
for i, post in enumerate(posts[:5], start=1):
    print(f"Пост №{i}")
    print("Заголовок:", post["title"])
    print("Текст:", post["body"])
    print("-" * 40)
