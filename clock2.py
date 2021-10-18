import time
import tkinter as tk
import datetime
from datetime import date, datetime

color = "#565567"

class Digital_clock():
    def __init__(self):
        self.mywindow = tk.Tk()
        self.mywindow.geometry("400x300")
        self.mywindow.resizable(0,0)
        self.mywindow.title("Relog | AlexanderJGA")
        self.mywindow.config(background='#1f2f3f')
        self.rectangle = tk.Label(text="x", font=('Tahoma', 9), fg=color, bg='#4B4B4B', pady=90, padx=134)
        self.current_time_label = tk.Label(text="", font=('Tahoma', 44), fg=color, bg='#DEDEDE', pady=10, padx=10)
        self.rectangle2 = tk.Label(text="x", font=('Tahoma', 12), fg=color, bg='#8B8B8B', pady=10, padx=123)
        self.week_day_label = tk.Label(text="", font=('Tahoma', 12), fg="white", bg='#8B8B8B', pady=10, padx=46)
        self.created_by_label = tk.Label(text="AlexanderJGA", font=('Tahoma', 9), fg="white", bg='#666666', pady=10, padx=89.5)
        self.current_time_label.place(x=70, y=50)
        self.rectangle2.place(x=70, y=145)
        self.week_day_label.place(x=70, y=145)
        self.created_by_label.place(x=70, y=188)
        self.rectangle.place(x=60, y=40)
        self.update_clock()
        self.get_date()
        self.mywindow.mainloop()

    def update_clock(self):
        tiempo = datetime.now()
        now = tiempo.strftime("%H:%M:%S")
        self.current_time_label.configure(text=now)
        self.mywindow.after(1000, self.update_clock)

    def get_date(self):
        # Get Week Day
        datetime_object = datetime.now()
        week_day = datetime_object.strftime("%A")

        # Get Current date
        today = datetime.now()
        d1 = today.strftime("%d/%m/%Y")
        self.week_day_label.configure(text = d1 + ' | ' + week_day)


main=Digital_clock()
