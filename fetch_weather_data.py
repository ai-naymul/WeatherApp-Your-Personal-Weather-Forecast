import requests as req
class FetchWeather:
    def __init__(self):
        self.API_KEY = "09a2c996cb784e8484e75654230408"
        self.temp = None
        self.humidity = None
        self.time = None
        self.status = None

    def fetch_weather(self, user_choice):
        try:
            response = req.get(f"http://api.weatherapi.com/v1/current.json?key={self.API_KEY}&q={user_choice}")
            response.raise_for_status()
        except req.RequestException as e:
            print(f"Request Failed due to Network Error. Error Code: {response.status_code}")
            return

        if response.status_code == 200:
            data = response.json()
            answer = data['current']
            self.time = answer['last_updated']
            self.temp = answer['temp_c']
            self.status = answer['condition']['text']
            self.humidity = answer["humidity"]
            output = f"Temperature: {self.temp} °F\n" \
                       f"Humidity: {self.humidity}%\n" \
                       f"Time: {self.time}\n" \
                       f"Conditions: {self.status}\n"
            print(output)


        elif response.status_code == 1006:
            print("No matching location found.")
        else:
            print(f"An error occurred. Status Code: {response.status_code}")


