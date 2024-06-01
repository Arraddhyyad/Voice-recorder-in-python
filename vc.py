from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import os

root = Tk()
root.geometry("600x700+400+80")
root.resizable(False, False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

def Record():
    try:
        dur = int(duration.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")
        return

    freq = 44100
    recording = sound.rec(dur * freq, samplerate=freq, channels=2)
    
  
    def countdown(temp):
        if temp > 0:
            countdown_label.config(text=f"{str(temp)}")
            root.after(1000, countdown, temp - 1)
        else:
            sound.wait()
            write("recording.wav", freq, recording)
            messagebox.showinfo("Time Countdown", "Time's up")

    countdown_label = Label(root, font="arial 40", width=4, background="#4a4a4a")
    countdown_label.grid(row=5, column=1, pady=20)
    countdown(dur)


Label(root, text="Voice Recorder", font="arial 30 bold", background="#4a4a4a", fg="white").grid(row=1, column=0, columnspan=3, pady=10)


duration = StringVar()
entry = Entry(root, textvariable=duration, font="arial 30", width=15)
entry.grid(row=2, column=0, columnspan=3, pady=10)

Label(root, text="Enter time in Seconds", font="arial 15", background="#4a4a4a", fg="white").grid(row=3, column=0, columnspan=3, pady=10)


record = Button(root, font="arial 20", text="Record", bg="#111111", fg="white", border=0, command=Record)
record.grid(row=4, column=0, columnspan=3, pady=20)


root.mainloop()
