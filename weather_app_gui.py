from tkinter import *
from fetch_weather_data import FetchWeather
import geocoder

tk = Tk()
weather = FetchWeather()
tk.title("WeatherApp - Your Personal Weather Forecast")
tk.minsize(width=400,height=200)
tk.config(padx=20,pady=10)


location = geocoder.ip('me')
latt = location.latlng[0]
lng = location.latlng[1]


## Weather fetching from the main file
def fetch_weather():
    USER_CHOICE = city_entry.get().title()
    weather.fetch_weather(USER_CHOICE)
    # Update labels with fetched weather data
    temp.config(text=f"Temperature: {weather.temp}")
    humidity.config(text=f"Humidity: {weather.humidity}%")
    time.config(text=f"Time: {weather.time}")
    condition.config(text=f"Condition: {weather.status}")

## Reset function
def reset():
    city_entry.delete(0, END)
    temp.config(text="Temperature: ")
    humidity.config(text="Humidity: ")
    time.config(text="Time: ")
    condition.config(text="Condition: ")


##Layout
city_label = Label(text="Enter The City Name: ")

city_entry = Entry()

fetch_data = Button(text='Fetch Weather', command=fetch_weather)

weather_label_frame = LabelFrame(text="Weather Info")

temp = Label(weather_label_frame,text="Temperature: ")

humidity = Label(weather_label_frame,text='Humidity: ')

time = Label(weather_label_frame,text="Time: ")

condition = Label(weather_label_frame,text="Condition: ")


reset_button = Button(text="Reset", command=reset, width=25)

get_current_location_weather = Button(text="Get Current Location Weather Info", width=31)

#Seting position

city_label.grid(row=0, column=0)
city_entry.grid(row=0, column=1)
fetch_data.grid(row=0,column=2,padx=20)
weather_label_frame.grid(row=2,column=0, columnspan=3, padx=20, pady=20, sticky="ew")
temp.grid(row=0, column=0, padx=10, pady=5, sticky="w")
humidity.grid(row=1,column=0,pady=5,padx=10,sticky='w')
time.grid(row=2,column=0,pady=5,padx=10,sticky='w')
condition.grid(row=3,column=0,padx=10,pady=5,sticky='w')

reset_button.grid(row=4,column=1, padx=10)

get_current_location_weather.grid(row=1,column=1, pady=10)
tk.mainloop()




