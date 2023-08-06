import requests as req
API_KEY = "09a2c996cb784e8484e7565423040"
USER_CHOICE = input('For which city would you like to have the weather? ').title()
try:
    response = req.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}8&q={USER_CHOICE}")
    response.raise_for_status()
except req.RequestException as e:
    print(f"Request Failed due to Nwtwokr Error.Error Code: {response.status_code}")
USER_CHOICE_TEMP = input('Which version of temparature do you want? ').lower()
if response.status_code == 200:
    data = response.json()
    answer = data['current']
    time = answer['last_updated']
    temp_c = answer['temp_c']
    temp_f = answer['temp_f']
    status = answer['condition']['text']
    humidity = answer["humidity"]
    if USER_CHOICE_TEMP == 'c':
        output_c = f"Temparature :{temp_c} °C \n" \
                 f"Humidity: {humidity}% \n" \
                 f"Time: {time} \n" \
                 f"Conditions: {status} \n"
        print(output_c)
    elif USER_CHOICE_TEMP == 'f':
        output_f = f"Temparature :{temp_f} °F \n" \
                   f"Humidity: {humidity}% \n" \
                   f"Time: {time} \n" \
                   f"Conditions: {status} \n"
        print(output_f)

elif response.status_code == 1006:
    print("No matching location found.")
else:
    print(f"Request failed with status code: {response.status_code}")