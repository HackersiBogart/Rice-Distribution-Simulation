import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import ImageTk, Image
import os

class StartingWindow(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.main_win_width = 1600
        self.font_size = 12
        self.master = master
        self.top_frame = ttk.Frame(width=self.main_win_width - 100, height=100)
        self.top_frame.pack(side=ttk.TOP)

        self.bottom_frame = ttk.Frame(width=self.main_win_width - 20, height=400)
        self.bottom_frame.pack(side=ttk.BOTTOM)


        image1 = Image.open("Are You Ready (2).png")
        test = ImageTk.PhotoImage(image1)
        image1 = image1.resize((50, 50))
        label1 = tk.Label(image=test)
        label1.image = test
        # Position image
        label1.place(x=500, y=20)
        self.start_btn()


    def start_btn(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=tk.X, expand=tk.YES, pady=(15, 10))

        strt_btn = ttk.Button(
            master=container,
            text="Start",
            command=self.start,
            bootstyle=SUCCESS,
            width=50,
        )
        strt_btn.pack(side=tk.LEFT, padx=(130, 5))
        strt_btn.focus_set()
        container.place(x=10, y=170)
    def start(self):
        """Initialize the DataEntryForm"""
        self.destroy()  # Destroy the starting window
        DataEntryForm(self.master)


class DataEntryForm(ttk.Frame):
    def __init__(self, master):
        self.master = master

        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.main_win_width = 1600
        self.font_size = 12
        self.top_frame = ttk.Frame(width=self.main_win_width - 100, height=100)
        self.top_frame.pack(side=ttk.TOP)
        self.bottom_frame = ttk.Frame(width=self.main_win_width - 20, height=400)
        self.bottom_frame.pack(side=ttk.BOTTOM)


        # form variables
        self.num_vehicles = ttk.StringVar(value="")
        self.starting_point = ttk.StringVar(value="")
        self.destination = ttk.StringVar(value="")

        # form header
        hdr_txt = "Please enter your contact information"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("Number of Vehicle", self.num_vehicles)
        self.create_form_entry("Select Starting Point", self.starting_point)
        self.create_form_entry("Select Destination", self.destination)
        self.create_buttonbox()

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=20)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        """Print the contents to console and return the values."""
        print("Number of Vehicles:", self.num_vehicles.get())
        print("Starting Point:", self.starting_point.get())
        print("Destination:", self.destination.get())
        return self.num_vehicles.get(), self.starting_point.get(), self.destination.get()

    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()



if __name__ == "__main__":

    start = ttk.Window("Rice Distribution Simulation", themename="superhero", resizable=(True, True))
    StartingWindow(start)
    start.mainloop()

