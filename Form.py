import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from pathlib import Path
from itertools import cycle
from PIL import Image, ImageTk, ImageSequence

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.place_window_center()
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def place_window_center(self):
        self.update_idletasks()
        w_height = self.winfo_height()
        w_width = self.winfo_width()
        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - w_width) // 2
        ypos = (s_height - w_height) // 2
        self.geometry(f'700x500+{xpos}+{ypos}')


class StartPage(tk.Frame):
    def __init__(self, parent, controller, themename="superhero", **kwargs):
        super().__init__(parent, **kwargs)
        self.style = ttk.Style(theme=themename)
        self.title = "Data Entry Form"
        frame = tk.Frame(self)
        frame.pack()
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller, themename="superhero", **kwargs):
        super().__init__(parent, **kwargs)
        self.style = ttk.Style(theme=themename)
        self.title = "Data Entry Form"
        frame = tk.Frame(self)
        frame.pack()

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        # Saving User Info
        user_info_frame = ttk.LabelFrame(frame, bootstyle="secondary", text="Data Input")
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        self.Start_point_label = tk.Label(user_info_frame, text="Starting Point")
        self.Start_point_combobox = ttk.Combobox(user_info_frame, values=["", "Daet", "Talisay", "Basud"])
        self.Start_point_label.grid(row=0, column=2)
        self.Start_point_combobox.grid(row=1, column=2)

        self.age_label = tk.Label(user_info_frame, text="Number of helper")
        self.age_spinbox = tk.Spinbox(user_info_frame, from_=1, to=110)
        self.age_label.grid(row=2, column=2)
        self.age_spinbox.grid(row=3, column=2)

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Destination Frame
        self.destination_frame = ttk.LabelFrame(frame, bootstyle="secondary", text="Destination Input")
        self.destination_frame.grid(row=1, column=0, sticky="news", padx=15, pady=10)

        # Initialize all_entries list
        self.all_entries = []

        # Button
        self.addboxButton = ttk.Button(self.destination_frame, bootstyle="info-outline", text="Add Destination", command=self.addBox)
        self.addboxButton.grid(row=0, column=2, sticky="news", padx=20, pady=10)

        self.showButton = ttk.Button(frame, bootstyle="info-outline", text="Start Simulation", command=self.startSimulation)
        self.showButton.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    def addBox(self):
        print("ADD")
        from_label = tk.Label(self.destination_frame, text='Destination')
        from_label.grid(row=len(self.all_entries) * 2, column=1)

        ent1 = ttk.Entry(self.destination_frame)
        ent1.grid(row=len(self.all_entries) * 2 + 1, column=1)

        to_label = tk.Label(self.destination_frame, text='Quantity')
        to_label.grid(row=len(self.all_entries) * 2, column=3)

        ent2 = tk.Spinbox(self.destination_frame, from_=1, to=110)
        ent2.grid(row=len(self.all_entries) * 2 + 1, column=3)

        self.all_entries.append((ent1, ent2))

    def showEntries(self):
        for number, (ent1, ent2) in enumerate(self.all_entries):
            print(number, ent1.get(), ent2.get())

    def startSimulation(self):
        # Destroy the current window
        self.destroy()

        # Create a new window for the animated GIF
        gif_window = ttk.Window()
        gif_window.title("Animated GIF")
        gif_window.geometry("700x500")

        # Create an instance of the AnimatedGif class in the new window
        animated_gif = AnimatedGif(gif_window, duration=5000)  # Specify the duration in milliseconds
        animated_gif.pack(fill=tk.BOTH, expand=tk.YES)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()


class AnimatedGif(ttk.Frame):
    def __init__(self, master, duration, **kwargs):
        super().__init__(master, **kwargs)
        self.duration = duration

        # open the GIF and create a cycle iterator
        file_path = Path(__file__).parent / "spinners.gif"
        with Image.open(file_path) as im:
            # create a sequence
            sequence = ImageSequence.Iterator(im)
            images = [ImageTk.PhotoImage(s) for s in sequence]
            self.image_cycle = cycle(images)

            # length of each frame
            self.framerate = im.info["duration"]

        self.img_container = ttk.Label(self, image=next(self.image_cycle))
        self.img_container.pack(fill=tk.BOTH, expand=tk.YES)
        self.after(self.framerate, self.next_frame)

    def next_frame(self):
        """Update the image for each frame"""
        self.img_container.configure(image=next(self.image_cycle))
        self.after(self.framerate, self.next_frame)

    def start_animation(self):
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.after(self.duration, self.destroy_master)  # Destroy master after the specified duration

    def destroy_master(self):
        if self.master and self.master.winfo_exists():
            self.master.destroy()


if __name__ == "__main__":
    app = SeaofBTCapp()
    app.mainloop()
