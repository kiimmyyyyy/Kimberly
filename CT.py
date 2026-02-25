import tkinter as tk
from tkinter import messagebox
import time


class CountdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Kimmy's Countdown Timer")


        self.time_seconds = tk.StringVar(value="")
        self.display_time = tk.StringVar(value="00:00:00")
        self.is_running = False



        self.input_label = tk.Label(master, text="Enter time in seconds:")
        self.input_label.pack(pady=10)


        self.input_entry = tk.Entry(master, textvariable=self.time_seconds, width=20)
        self.input_entry.pack(pady=5)
m

        self.display_label = tk.Label(master,
                                      textvariable=self.display_time,
                                      font=("Helvetica", 48),
                                      fg="pink")
        self.display_label.pack(pady=20)


        self.start_button = tk.Button(master, text="Start Countdown", command=self.start_countdown, bg="green",
                                      fg="white")
        self.start_button.pack(pady=15)


        self.stop_button = tk.Button(master, text="Stop", command=self.stop_countdown, state=tk.DISABLED, bg="red",
                                     fg="white")
        self.stop_button.pack(pady=15)

    def start_countdown(self):

        try:
            kimmys_time = int(self.time_seconds.get())
        except ValueError:
            messagebox.showerror(title="Invalid Input", message= "Please enter a valid number for the time in seconds.")
            return

        if kimmys_time <= 0:
            messagebox.showerror(title="Invalid Input", message= "Time must be greater than 0 seconds.")
            return

        self.input_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.current_time = kimmys_time
        self.is_running = True
        self.update_timer()

    def stop_countdown(self):

        self.is_running = False
        self.input_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.display_time.set("Stopped")

    def update_timer(self):

        if not self.is_running:
            return

        if self.current_time > 0:

            hours = self.current_time // 3600
            minutes = (self.current_time % 3600) // 60
            seconds = self.current_time % 60


            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.display_time.set(time_str)


            self.current_time -= 1


            self.master.after(1000, self.update_timer)
        else:

            self.display_time.set("DONE NAAAA")
            messagebox.showinfo(title="Countdown Complete", message= "DONE NAAAA")


            self.is_running = False
            self.input_entry.config(state=tk.NORMAL)
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)


root = tk.Tk()
app = CountdownApp(root)
root.mainloop()import tkinter as tk
from tkinter import messagebox
import time


class CountdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Kimmy's Countdown Timer")


        self.time_seconds = tk.StringVar(value="")
        self.display_time = tk.StringVar(value="00:00:00")
        self.is_running = False



        self.input_label = tk.Label(master, text="Enter time in seconds:")
        self.input_label.pack(pady=10)


        self.input_entry = tk.Entry(master, textvariable=self.time_seconds, width=20)
        self.input_entry.pack(pady=5)


        self.display_label = tk.Label(master,
                                      textvariable=self.display_time,
                                      font=("Helvetica", 48),
                                      fg="pink")
        self.display_label.pack(pady=20)


        self.start_button = tk.Button(master, text="Start Countdown", command=self.start_countdown, bg="green",
                                      fg="white")
        self.start_button.pack(pady=15)


        self.stop_button = tk.Button(master, text="Stop", command=self.stop_countdown, state=tk.DISABLED, bg="red",
                                     fg="white")
        self.stop_button.pack(pady=15)

    def start_countdown(self):

        try:
            kimmys_time = int(self.time_seconds.get())
        except ValueError:
            messagebox.showerror(title="Invalid Input", message= "Please enter a valid number for the time in seconds.")
            return

        if kimmys_time <= 0:
            messagebox.showerror(title="Invalid Input", message= "Time must be greater than 0 seconds.")
            return

        self.input_entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.current_time = kimmys_time
        self.is_running = True
        self.update_timer()

    def stop_countdown(self):

        self.is_running = False
        self.input_entry.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.display_time.set("Stopped")

    def update_timer(self):

        if not self.is_running:
            return

        if self.current_time > 0:

            hours = self.current_time // 3600
            minutes = (self.current_time % 3600) // 60
            seconds = self.current_time % 60


            time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.display_time.set(time_str)


            self.current_time -= 1


            self.master.after(1000, self.update_timer)
        else:

            self.display_time.set("DONE NAAAA")
            messagebox.showinfo(title="Countdown Complete", message= "DONE NAAAA")


            self.is_running = False
            self.input_entry.config(state=tk.NORMAL)
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)


root = tk.Tk()
app = CountdownApp(root)
root.mainloop()