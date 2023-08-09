from tkinter import *

tk = Tk()
tk.title("WeatherApp - Your Personal Weather Forecast")
tk.minsize(width=500,height=300)

city_label = Label(text="Enter The City Name: ")
city_label.grid(row=0, column=0, padx=0, pady=10)
city_entry = Entry()
city_entry.grid(row=0, column=1, padx=0, pady=10)




tk.mainloop()












