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

print("Starting application...")

def Record():
    print("Record button clicked")
    try:
        dur = int(duration.get())
        print(f"Duration entered: {dur} seconds")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")
        print("Invalid input for duration")
        return

    freq = 44100
    
    try:
        device_info = sound.query_devices(None, 'input')
        max_channels = device_info['max_input_channels']
        channels = 2 if max_channels >= 2 else 1
        print(f"Max input channels: {max_channels}, using {channels} channel(s)")
    except Exception as e:
        messagebox.showerror("Error", f"Could not query input device: {e}")
        print(f"Error querying input device: {e}")
        return

    recording = sound.rec(dur * freq, samplerate=freq, channels=channels)
    
    def countdown(temp):
        if temp > 0:
            countdown_label.config(text=f"{str(temp)}")
            root.after(1000, countdown, temp - 1)
        else:
            sound.wait()
            write("recording.wav", freq, recording)
            messagebox.showinfo("Time Countdown", "Time's up")
            print("Recording saved as 'recording.wav'")

    countdown_label = Label(root, font="arial 40", width=4, background="#4a4a4a")
    countdown_label.grid(row=5, column=1, pady=20)
    countdown(dur)

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "image.png")

print(f"Image path: {image_path}")

if not os.path.isfile(image_path):
    raise FileNotFoundError(f"Image file '{image_path}' not found. Please check the file path.")
else:
    try:
        image_icon = PhotoImage(file=image_path)
        print("Image loaded successfully")
    except Exception as e:
        raise Exception(f"Error loading image '{image_path}': {e}")

root.iconphoto(False, image_icon)

photo = PhotoImage(file=image_path)
myimage = Label(root, image=photo, background="#4a4a4a")
myimage.grid(row=0, column=0, columnspan=3, pady=10)

Label(root, text="Voice Recorder", font="arial 30 bold", background="#4a4a4a", fg="white").grid(row=1, column=0, columnspan=3, pady=10)

duration = StringVar()
entry = Entry(root, textvariable=duration, font="arial 30", width=15)
entry.grid(row=2, column=0, columnspan=3, pady=10)

Label(root, text="Enter time in Seconds", font="arial 15", background="#4a4a4a", fg="white").grid(row=3, column=0, columnspan=3, pady=10)

record = Button(root, font="arial 20", text="Record", bg="#111111", fg="white", border=0, command=Record)
record.grid(row=4, column=0, columnspan=3, pady=20)

print("Application setup complete, entering main loop.")
root.mainloop()
print("Application closed.")
