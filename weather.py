import requests

# ВСТАВЬ СЮДА СВОЙ API-KEY OpenWeather
API_KEY = "YOUR_API_KEY"

city = input("Введите название города: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",  # температура в °C
    "lang": "ru",  # описание на русском
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    print(f"Город: {city}")
    print(f"Температура: {temperature} °C")
    print(f"Описание: {description}")

elif response.status_code == 404:
    print("Город не найден.")
elif response.status_code == 401:
    print("Ошибка: неверный API ключ (Unauthorized).")
else:
    print(f"Ошибка получения данных: {response.status_code}")
