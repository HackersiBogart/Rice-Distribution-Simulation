import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import messagebox


class DataEntryForm(tk.Tk):
    def __init__(
        self,
        title="Data Entry Form",
        themename="superhero",
        iconphoto='',
        size=None,
        position=None,
        minsize=None,
        maxsize=None,
        resizable=None,
        hdpi=True,
        scaling=None,
        transient=None,
        overrideredirect=False,
        alpha=1.0,
    ):
        super().__init__()
        self.style = ttk.Style(theme=themename)
        self.title(title)
        self.geometry("700x500")  # Set your preferred size
        self.place_window_center()
        frame = tk.Frame(self)
        frame.pack()

        # Saving User Info
        user_info_frame = ttk.LabelFrame(frame, bootstyle="secondary", text="Data Input")
        user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        self.Start_point_label = tk.Label(user_info_frame, text="Starting Pont")
        self.Start_point_combobox = ttk.Combobox(user_info_frame, values=["", "Daet", "Talisay", "Basud"])
        self.Start_point_label.grid(row=0, column=0)
        self.Start_point_combobox.grid(row=1, column=0)
        self.destination_label = tk.Label(user_info_frame, text="Destination")
        self.destination_combobox = ttk.Combobox(user_info_frame, values=["", "Daet", "Talisay", "Basud"])
        self.destination_label.grid(row=0, column=1)
        self.destination_combobox.grid(row=1, column=1)

        self.title_label = tk.Label(user_info_frame, text="Distance")
        self.distance_entry = ttk.Entry(user_info_frame)
        self.title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
        self.title_label.grid(row=0, column=2)
        self.title_combobox.grid(row=1, column=2)

        self.age_label = tk.Label(user_info_frame, text="Age")
        self.age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
        self.age_label.grid(row=2, column=0)
        self.age_spinbox.grid(row=3, column=0)

        self.nationality_label = tk.Label(user_info_frame, text="Nationality")
        self.nationality_combobox = ttk.Combobox(user_info_frame,
                                                 values=["Africa", "Antarctica", "Asia", "Europe", "North America",
                                                         "Oceania",
                                                         "South America"])
        self.nationality_label.grid(row=2, column=1)
        self.nationality_combobox.grid(row=3, column=1)

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Saving Course Info
        self.courses_frame = ttk.LabelFrame(frame, bootstyle="secondary", text="Registration Status")
        self.courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.registered_label = tk.Label(self.courses_frame )

        self.reg_status_var = tk.StringVar(value="Not Registered")
        self.registered_check = tk.Checkbutton(self.courses_frame, text="Currently Registered",
                                               variable=self.reg_status_var, onvalue="Registered", offvalue="Not registered")

        self.registered_label.grid(row=0, column=0)
        self.registered_check.grid(row=1, column=0)

        self.numcourses_label = tk.Label(self.courses_frame, text="# Completed Courses")
        self.numcourses_spinbox = tk.Spinbox(self.courses_frame, from_=0, to='infinity')
        self.numcourses_label.grid(row=0, column=1)
        self.numcourses_spinbox.grid(row=1, column=1)

        self.numsemesters_label = tk.Label(self.courses_frame, text="# Semesters")
        self.numsemesters_spinbox = tk.Spinbox(self.courses_frame, from_=0, to="infinity")
        self.numsemesters_label.grid(row=0, column=2)
        self.numsemesters_spinbox.grid(row=1, column=2)

        for widget in self.courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Accept terms
        self.terms_frame = ttk.LabelFrame(frame, bootstyle="secondary", text="Terms & Conditions")
        self.terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        self.accept_var = tk.StringVar(value="Not Accepted")
        self.terms_check = tk.Checkbutton(self.terms_frame, text="I accept the terms and conditions.",
                                          variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        self.terms_check.grid(row=0, column=0)

        # Button
        self.button = ttk.Button(frame, bootstyle="info-outline", text="Enter data", command=self.enter_data)
        self.button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def place_window_center(self):
        """Position the toplevel in the center of the screen. Does not
        account for titlebar height."""
        self.update_idletasks()
        w_height = self.winfo_height()
        w_width = self.winfo_width()
        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - w_width) // 2
        ypos = (s_height - w_height) // 2
        self.geometry(f'+{xpos}+{ypos}')

    def enter_data(self):
        accepted = self.accept_var.get()

        if accepted == "Accepted":
            # User info
            firstname = self.first_name_entry.get()
            lastname = self.last_name_entry.get()

            if firstname and lastname:
                title = self.title_combobox.get()
                age = self.age_spinbox.get()
                nationality = self.nationality_combobox.get()

                # Course info
                registration_status = self.reg_status_var.get()
                numcourses = self.numcourses_spinbox.get()
                numsemesters = self.numsemesters_spinbox.get()

                print("First name: ", firstname, "Last name: ", lastname)
                print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
                print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
                print("Registration status", registration_status)
                print("------------------------------------------")
            else:
                tk.messagebox.showwarning(title="Error", message="First name and last name are required.")
        else:
            tk.messagebox.showwarning(title="Error", message="You have not accepted the terms")


if __name__ == "__main__":

    app = DataEntryForm()
    app.mainloop()
