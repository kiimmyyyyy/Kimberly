import tkinter as tk
from tkinter import messagebox
import threading
from playsound import playsound


class CountdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Kimmy's Countdown Timer")


        self.time_seconds = tk.StringVar(value="")
        self.display_time = tk.StringVar(value="00:00:00")
        self.is_running = False
        self.current_time = 0



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


        self.stop_button = tk.Button(master, text="Stop", command=self.stop_countdown, state="disabled", bg="red", fg="white")
        self.stop_button.pack(pady=15)

    def start_countdown(self):

        try:
            kimmy_time = int(self.time_seconds.get())
        except ValueError:
            messagebox.showerror(title="Invalid Input", message= "Please enter a valid number for the time in seconds.")
            return

        if kimmy_time <= 0:
            messagebox.showerror(title="Invalid Input", message= "Time must be greater than 0 seconds.")
            return

        self.input_entry.config(state="disabled")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        self.current_time = kimmy_time
        self.is_running = True
        self.update_timer()

    def stop_countdown(self):

        self.is_running = False
        self.input_entry.config(state="normal")
        self.start_button.config(state="normal")
        self.stop_button.config(state="normal")
        self.display_time.set("Stopped")

    @staticmethod
    def play_alarm_sound():
        try:
            playsound('alarm.mp3')
        except Exception as e:
            print(f"Error: {e}")

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
            self.display_time.set("DONE NA")

            sound_thread = threading.Thread(target=self.play_alarm_sound, daemon=True)
            sound_thread.start()
            messagebox.showinfo(title="Countdown Complete", message="DONE NA")

            self.is_running = False
            self.input_entry.config(state="normal")
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")


root = tk.Tk()
app = CountdownApp(root)
root.mainloop()