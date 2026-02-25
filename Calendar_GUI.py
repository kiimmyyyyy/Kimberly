from tkinter import *
from tkcalendar import *


root = Tk()

def choice_date():
    present_date = display_cal.get_date()
    user_date = Label(text=present_date)
    user_date.pack(padx=2,pady=2)


display_cal = Calendar(root, setmode="day", date_pattern='d/m/yy')
display_cal.pack(padx=15,pady=15)

open_cal = Button(root, text='select date', command=choice_date)
open_cal.pack(padx=15,pady=15)

root.geometry("400x400")
root.title("GUI CALENDAR")
root.configure(bg="red")
root.mainloop()
