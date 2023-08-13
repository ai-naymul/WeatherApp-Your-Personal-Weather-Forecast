from tkinter import *

tk = Tk()
tk.title("WeatherApp - Your Personal Weather Forecast")
tk.minsize(width=400,height=200)
tk.config(padx=20,pady=10)

city_label = Label(text="Enter The City Name: ")
city_label.grid(row=0, column=0)

city_entry = Entry()
city_entry.grid(row=0, column=1)

fetch_data = Button(text='Fetch Weather')
fetch_data.grid(row=0,column=2,padx=20)

weather_label_frame = LabelFrame(text="Weather Info")
weather_label_frame.grid(row=1,column=0, columnspan=3, padx=20, pady=20, sticky="ew")


temp = Label(weather_label_frame,text="Temperature: ")
temp.grid(row=0, column=0, padx=10, pady=5, sticky="w")


humidity = Label(weather_label_frame,text='Humidity: ')
humidity.grid(row=1,column=0,pady=5,padx=10,sticky='w')

time = Label(weather_label_frame,text="Time: ")
time.grid(row=2,column=0,pady=5,padx=10,sticky='w')

condition = Label(weather_label_frame,text="Condition: ")
condition.grid(row=3,column=0,padx=10,pady=5,sticky='w')


tk.mainloop()



