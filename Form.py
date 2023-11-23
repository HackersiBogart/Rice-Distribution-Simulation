import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from pathlib import Path
from itertools import cycle
from PIL import Image, ImageTk, ImageSequence
import os

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)
        container.pack_propagate(False)  # Disable resizing of the container
        self.place_window_center()
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.pack(fill=tk.BOTH, expand=True)

        # Set the size of each page frame to be the same as the window size
        for frame in self.frames.values():
            frame.pack_propagate(False)
            frame.config(width=self.winfo_screenwidth(), height=self.winfo_screenheight())

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.place_forget()  # Hide the current frame
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)  # Plac

    def place_window_center(self):
        window_width = 900
        window_height = 600

        self.update_idletasks()
        w_height = self.winfo_height()
        w_width = self.winfo_width()
        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - window_width) // 2
        ypos = (s_height - window_height) // 2
        self.geometry(f'{window_width}x{window_height}+{xpos}+{ypos}')


class StartPage(tk.Frame):
    def __init__(self, parent, controller, themename="superhero", **kwargs):
        tk.Frame.__init__(self,parent)
        self.style = ttk.Style(theme=themename)
        self.title = "Data Entry Form"

        image_path = "Are You Ready (2).png"
        if os.path.exists(image_path):
            self.image1 = Image.open(image_path)
            resize_image = self.image1.resize((500, 500))  # Adjust the size as needed
            img = ImageTk.PhotoImage(resize_image)

            # Create label and add resized image
            self.label1 = ttk.Label(self, image=img)
            self.label1.image = img
            self.label1.pack(expand=True)  # Use pack to center the image


        self.button = ttk.Button(self,bootstyle="info",text="Let's Start", width= 50,command=lambda: controller.show_frame(PageOne))
        self.button.pack(side=TOP,anchor=S)
        self.button.place(relx=.5, rely=.7, anchor="c")

        self.button2 = ttk.Button(self, bootstyle="danger-outline", text="Exit",width= 50, command=lambda: controller.show_frame(PageTwo))
        self.button2.pack(side=TOP, anchor=S)
        self.button2.place(relx=.5, rely=.77, anchor="c")



class PageOne(tk.Frame):
    def __init__(self, parent, controller, themename="superhero", **kwargs):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style(theme=themename)
        self.title = "Data Entry Form"
        button1 = ttk.Button(self, bootstyle="info-outline", text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)
        # Saving User Info
        user_info_frame = ttk.LabelFrame(self, bootstyle="secondary", text="Data Input")
        user_info_frame.pack(side=tk.LEFT, padx=20, pady=10)

        self.Start_point_label = tk.Label(user_info_frame, text="Starting Point")
        self.Start_point_combobox = ttk.Combobox(user_info_frame, values=["", "Daet", "Talisay", "Basud"])
        self.Start_point_label.pack(side=tk.TOP, padx=10, pady=5)
        self.Start_point_combobox.pack(side=tk.TOP, padx=10, pady=5)

        self.age_label = tk.Label(user_info_frame, text="Number of helper")
        self.age_spinbox = tk.Spinbox(user_info_frame, from_=1, to=110)
        self.age_label.pack(side=tk.TOP, padx=10, pady=5)
        self.age_spinbox.pack(side=tk.TOP, padx=10, pady=5)

        # Destination Frame
        self.destination_frame = ttk.LabelFrame(self, bootstyle="secondary", text="Destination Input")
        self.destination_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Create a canvas inside the destination_frame
        self.canvas = tk.Canvas(self.destination_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a frame to hold the widgets inside the canvas
        self.inner_frame = ttk.Frame(self.canvas)
        self.inner_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar and associate it with the canvas
        self.yscrollbar = ttk.Scrollbar(self.destination_frame, bootstyle="info-round", orient="vertical",
                                        command=self.canvas.yview)
        self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)

        # Configure the canvas to scroll the inner_frame
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor=tk.NW)

        # Bind the canvas to the scroll region
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Add this line to handle the inner frame's resizing
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Initialize all_entries list
        self.all_entries = []
        self.all_labels = []


        # Button


        self.addboxButton = ttk.Button(self.destination_frame, bootstyle="info-outline", text="Add Destination",
                                       command=self.addBox)
        self.addboxButton.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

        self.removeBoxButton = ttk.Button(self.destination_frame, bootstyle="danger-outline", text="Remove Last Box",
                                          command=self.removeLastBox)
        self.removeBoxButton.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)
        button2 = ttk.Button(self, bootstyle="info-outline", text="Start Simulation",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)
    def addBox(self):
        entry_frame = ttk.Frame(self.inner_frame)
        entry_frame.pack(side=tk.TOP, padx=10, pady=5, fill=tk.X)

        from_label = tk.Label(entry_frame, text='Destination')
        from_label.pack(side=tk.LEFT)

        ent1 = ttk.Entry(entry_frame)
        ent1.pack(side=tk.LEFT, padx=5)

        to_label = tk.Label(entry_frame, text='Quantity')
        to_label.pack(side=tk.LEFT, padx=5)

        ent2 = tk.Spinbox(entry_frame, from_=1, to=110)
        ent2.pack(side=tk.LEFT, padx=5)

        self.all_entries.append((ent1, ent2))
        self.all_labels.append((from_label, to_label))

        # Update the scroll region of the canvas
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Add this line to handle the inner frame's resizing
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    def removeLastBox(self):
        if self.all_entries:
            ent1, ent2 = self.all_entries.pop()
            ent1.destroy()
            ent2.destroy()

        if self.all_labels:
            from_label, to_label = self.all_labels.pop()
            from_label.destroy()
            to_label.destroy()

        # Update the scroll region of the canvas
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Add this line to handle the inner frame's resizing
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    def showEntries(self):
        for number, (ent1, ent2) in enumerate(self.all_entries):
            print(number, ent1.get(), ent2.get())


class PageTwo(tk.Frame):
    def __init__(self, parent, controller, themename="superhero", duration=5000):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style(theme=themename)

        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, bootstyle="info-outline", text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)



        self.style = ttk.Style(theme="superhero")

        # Center the GIF
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.duration = duration

        # open the GIF and create a cycle iterator
        file_path = Path(__file__).parent / "distributor_to_store.gif"
        with Image.open(file_path) as im:
            # create a sequence
            sequence = ImageSequence.Iterator(im)
            images = [ImageTk.PhotoImage(s) for s in sequence]
            self.image_cycle = cycle(images)

            # length of each frame
            self.framerate = im.info["duration"]

        self.img_container = ttk.Label(self, image=next(self.image_cycle))
        self.img_container.pack(fill=tk.BOTH, expand=True)  # Expand to fill available space
        self.img_container.bind("<Configure>", self.center_gif)
        self.after(self.framerate, self.next_frame)
        button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()
        button2 = ttk.Button(self, bootstyle="info-outline", text="See Result",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack(side=tk.RIGHT, anchor="se", padx=20, pady=30)

    def next_frame(self):
        """Update the image for each frame"""
        self.img_container.configure(image=next(self.image_cycle))
        self.after(self.framerate, self.next_frame)

    def center_gif(self, event):
        """Center the GIF when the container size changes"""
        width = 900
        height = 600

        # Get the size of the image
        image_width = self.img_container.winfo_reqwidth()
        image_height = self.img_container.winfo_reqheight()

        # Calculate the position to center the image
        x = (width - image_width) // 2
        y = (height - image_height) // 2

        # Set the new position
        self.img_container.place(x=x, y=y)





if __name__ == "__main__":
    app = SeaofBTCapp()
    app.mainloop()
