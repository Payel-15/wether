import requests
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def get_weather(city_name):
    api_key = "openweathermap_api_key" #use your own api key here
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            speak(f"City '{city_name}' not found.")
        else:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            speak(f"The current temperature in {city_name} is {temp}°C with {desc}.")
    except Exception as e:
        speak("Unable to fetch weather data. Please check your connection or API key.")
        print(e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
