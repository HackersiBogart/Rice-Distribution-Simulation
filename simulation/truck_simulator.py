import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk, ImageSequence
import os
from ttkbootstrap.tableview import Tableview

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)
        container.pack_propagate(True)  # Disable resizing of the container
        self.title("Rice Distribution Simulator ")
        self.place_window_center()
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, SimulationResultPage):
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
        window_width = 1200
        window_height = 620

        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - window_width) // 2
        ypos = (s_height - window_height) // 2

        self.geometry(f'{window_width}x{window_height}+{xpos}+{ypos}')
        self.update_idletasks()


class StartPage(tk.Frame):
    def __init__(self, parent, controller, themename="superhero", **kwargs):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style(theme=themename)
        self.title = "Data Entry Form"

        image_path = "C:\\Users\\admin\\PycharmProjects\\Rice-Distribution-Simulation\\simulation\\RDS Logo.png"
        if os.path.exists(image_path):
            self.image1 = Image.open(image_path)
            resize_image = self.image1.resize((500, 500))  # Adjust the size as needed
            img = ImageTk.PhotoImage(resize_image)

            # Create label and add resized image
            self.label1 = ttk.Label(self, image=img)
            self.label1.image = img
            self.label1.pack(side=TOP, anchor=N, expand=True)  # Use pack to center the image
            self.label1.place(relx=.5, rely=.4, anchor="c")

        self.button = ttk.Button(self, bootstyle="info", text="Let's Start", width=50,
                                 command=lambda: controller.show_frame(PageOne))
        self.button.pack(side=TOP, anchor=S)
        self.button.place(relx=.5, rely=.7, anchor="c")  # Adjusted rely value

        self.button2 = ttk.Button(self, bootstyle="danger-outline", text="Exit", width=50,
                                  command=lambda: controller.show_frame(PageTwo))
        self.button2.pack(side=TOP, anchor=S)
        self.button2.place(relx=.5, rely=.78, anchor="c")  # Adjusted rely value


D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2
D1_to_M1_time = 2

D2_to_M1_time = 2
D2_to_M2_time = 2
D2_to_M3_time = 2
D2_to_M4_time = 2
D2_to_M5_time = 2
D2_to_M6_time = 2
D2_to_M7_time = 2
D2_to_M8_time = 2
D2_to_M9_time = 2
D2_to_M10_time = 2
D2_to_M11_time = 2
D2_to_M12_time = 2
D2_to_M13_time = 2
D2_to_M14_time = 2

D3_to_M1_time = 2
D3_to_M2_time = 2
D3_to_M3_time = 2
D3_to_M4_time = 2
D3_to_M5_time = 2
D3_to_M6_time = 2
D3_to_M7_time = 2
D3_to_M8_time = 2
D3_to_M9_time = 2
D3_to_M10_time = 2
D3_to_M11_time = 2
D3_to_M12_time = 2
D3_to_M13_time = 2
D3_to_M14_time = 2


class PageOne(tk.Frame):

    def __init__(self, parent, controller, themename="superhero", **kwargs):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style(theme=themename)
        self.title = "Data Entry Form"
        # Initialize a variable to keep track of the y-coordinate
        self.last_removed_y = 0
        self.entry_frames = []
        button1 = ttk.Button(self, bootstyle="info-outline", text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)
        # Saving User Info
        user_info_frame = ttk.LabelFrame(self, bootstyle="secondary", text="Data Input", width=100, height=100)
        user_info_frame.pack(side=tk.LEFT, padx=20, pady=10)

        self.Start_point_label = tk.Label(user_info_frame, text="Starting Point")
        self.Start_point_combobox = ttk.Combobox(user_info_frame, values=["", "D1", "D2", "D3"])
        self.Start_point_label.pack(side=tk.TOP, padx=10, pady=5)
        self.Start_point_combobox.pack(side=tk.TOP, padx=10, pady=5)
        self.age_label = tk.Label(user_info_frame, text="Number of helper")
        self.age_spinbox = tk.Spinbox(user_info_frame, from_=1, to=110)
        self.age_label.pack(side=tk.TOP, padx=10, pady=5)
        self.age_spinbox.pack(side=tk.TOP, padx=10, pady=5)

        # Destination Frame
        self.destination_frame = ttk.LabelFrame(self, bootstyle="secondary", text="Destination Input", width=200,
                                                height=200)
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

        ent1 = ttk.Combobox(entry_frame,
                            values=["", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12",
                                    "M13", "M14", ])
        ent1.pack(side=tk.LEFT, padx=5)

        to_label = tk.Label(entry_frame, text='Quantity')
        to_label.pack(side=tk.LEFT, padx=5)

        ent2 = tk.Spinbox(entry_frame, from_=1, to=110)
        ent2.pack(side=tk.LEFT, padx=5)

        self.entry_frames.append(entry_frame)

        # Update the scroll region of the canvas
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Add this line to handle the inner frame's resizing
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def removeLastBox(self):
        if self.entry_frames:
            entry_frame = self.entry_frames.pop()
            entry_frame.destroy()

        # Update the scroll region of the canvas
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Add this line to handle the inner frame's resizing
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


class PageTwo(tk.Frame):
    def __init__(self, parent, controller, themename="superhero", **kwargs):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style(theme=themename)
        self.title = "Truck Movement Simulation"
        button1 = ttk.Button(self, bootstyle="info-outline", text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)
        result_button = ttk.Button(self, bootstyle="info-outline", text="show results",
                                   command=lambda: controller.show_frame(SimulationResultPage))
        result_button.pack(side=tk.BOTTOM, anchor="se", padx=10, pady=10)

        # Add the provided truck movement simulation code here

        roads = [
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0),
            (13, 0), (14, 0), (15, 0), (16, 0), (17, 0),
            (0, 1), (6, 1), (9, 1), (13, 1), (17, 1),
            (0, 2), (6, 2), (9, 2), (13, 2), (17, 2),
            (0, 3), (6, 3), (9, 3), (13, 3), (17, 3),
            (0, 4), (6, 4), (9, 4), (13, 4), (17, 4),
            (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5),
            (13, 5), (14, 5), (15, 5), (16, 5), (17, 5),
            (0, 6), (6, 6), (13, 6), (17, 6),
            (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (13, 7), (17, 7),
            (0, 8), (6, 8), (13, 8), (17, 8),
            (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9),
            (13, 9), (14, 9), (15, 9), (16, 9), (17, 9)
        ]

        # Function to load character images for different directions
        def load_character_images():
            character_images = {
                "up": tk.PhotoImage(
                    file="C:\\Users\\admin\\PycharmProjects\\Rice-Distribution-Simulation\\simulation\\up.png"),
                "down": tk.PhotoImage(
                    file="C:\\Users\\admin\\PycharmProjects\\Rice-Distribution-Simulation\\simulation\\down.png"),
                "left": tk.PhotoImage(
                    file="C:\\Users\\admin\\PycharmProjects\\Rice-Distribution-Simulation\\simulation\\left.png"),
                "right": tk.PhotoImage(
                    file="C:\\Users\\admin\\PycharmProjects\\Rice-Distribution-Simulation\\simulation\\right.png")
            }
            return character_images

        def move_truck(canvas, start, destination, character_images, map_image, map_scale):
            global truck, move_next_func
            truck = None
            move_next_func = None
            truck_width = 50
            truck_images = {
                "up": character_images["up"],
                "down": character_images["down"],
                "left": character_images["left"],
                "right": character_images["right"]
            }

            if truck:
                canvas.delete(truck)

            truck = canvas.create_image(start[0] * truck_width, start[1] * truck_width, anchor="nw",
                                        image=truck_images["right"])
            current_position = start
            current_direction = "right"

            def move_next():
                nonlocal truck_images, current_position, current_direction
                if current_position != destination:
                    next_move = (destination[0] - current_position[0], destination[1] - current_position[1])
                    move_x = 1 if next_move[0] > 0 else -1 if next_move[0] < 0 else 0
                    move_y = 1 if next_move[1] > 0 else -1 if next_move[1] < 0 else 0

                    new_x = current_position[0] + move_x
                    new_y = current_position[1] + move_y

                    if (new_x, new_y) in roads:
                        canvas.move(truck, move_x * truck_width, move_y * truck_width)
                        current_position = (new_x, new_y)

                        if move_x == 1:
                            current_direction = "right"
                        elif move_x == -1:
                            current_direction = "left"
                        elif move_y == 1:
                            current_direction = "down"
                        elif move_y == -1:
                            current_direction = "up"

                        canvas.itemconfig(truck, image=truck_images[current_direction])
                    else:
                        if current_position == (1, 5) and destination == (5, 0):
                            canvas.move(truck, 0, -1 * truck_width)
                            current_position = (1, 4)
                            current_direction = "up"
                            canvas.itemconfig(truck, image=truck_images[current_direction])
                        elif current_position == (0, 0) and destination == (7, 9):
                            canvas.move(truck, 1 * truck_width, 0)
                            current_position = (1, 0)
                            current_direction = "right"
                            canvas.itemconfig(truck, image=truck_images[current_direction])
                        elif current_position == (7, 9) and destination == (0, 9):
                            canvas.move(truck, 0, 1 * truck_width)
                            current_position = (0, 9)
                            current_direction = "down"
                            canvas.itemconfig(truck, image=truck_images[current_direction])
                        elif current_position == (1, 0) and destination == (7, 9):
                            canvas.move(truck, 1 * truck_width, 0)
                            current_position = (7, 9)
                            current_direction = "right"
                            canvas.itemconfig(truck, image=truck_images[current_direction])
                        elif current_position == (0, 5) and destination == (0, 9):
                            canvas.move(truck, 0, 1 * truck_width)
                            current_position = (0, 6)
                            current_direction = "down"
                            canvas.itemconfig(truck, image=truck_images[current_direction])
                        elif current_position == (0, 9) and destination == (0, 5):
                            canvas.move(truck, 0, -1 * truck_width)
                            current_position = (0, 8)
                            current_direction = "up"
                            canvas.itemconfig(truck, image=truck_images[current_direction])
                        else:
                            new_x_vert = current_position[0]
                            new_y_vert = current_position[1] + move_y

                            if (new_x_vert, new_y_vert) in roads:
                                canvas.move(truck, 0, move_y * truck_width)
                                current_position = (new_x_vert, new_y_vert)

                                if move_y == 1:
                                    current_direction = "down"
                                elif move_y == -1:
                                    current_direction = "up"

                                canvas.itemconfig(truck, image=truck_images[current_direction])
                            else:
                                new_x_horiz = current_position[0] + move_x
                                new_y_horiz = current_position[1]

                                if (new_x_horiz, new_y_horiz) in roads:
                                    canvas.move(truck, move_x * truck_width, 0)
                                    current_position = (new_x_horiz, new_y_horiz)

                                    if move_x == 1:
                                        current_direction = "right"
                                    elif move_x == -1:
                                        current_direction = "left"

                                    canvas.itemconfig(truck, image=truck_images[current_direction])

                    move_next_func = canvas.after(50, move_next)

            move_next()

        def reset_simulation():
            global truck, move_next_func
            if truck:
                canvas.delete(truck)  # Remove existing truck image
                canvas.after_cancel(move_next_func)  # Stop the movement function if running

        def start_movement():
            input_sequence = input_sequence_entry.get()  # Get the sequence entered by the user
            sequence = input_sequence.split(",")  # Split the input into a list of points

            positions = {
                "D1": (0, 2),
                "D2": (0, 6),
                "D3": (0, 9),
                "M1": (5, 0),
                "M2": (8, 0),
                "M3": (11, 0),
                "M4": (10, 5),
                "M5": (16, 0),
                "M6": (14, 5),
                "M7": (5, 9),
                "M8": (7, 5),
                "M9": (12, 5),
                "M10": (7, 9),
                "M11": (10, 9),
                "M12": (14, 9),
                "M13": (16, 5),
                "M14": (18, 9),
            }

            sequence_positions = [positions.get(point.strip()) for point in sequence]
            sequence_positions = [pos for pos in sequence_positions if pos is not None]

            if sequence_positions:
                move_truck_sequence(canvas, sequence_positions, load_character_images(), map_image, map_scale)
            else:
                print("Invalid sequence of points")

        def move_truck_sequence(canvas, sequence_positions, character_images, map_image, map_scale):
            def move_to_next_position(start_pos, sequence_positions):
                if not sequence_positions:
                    return

                if start_pos is None:
                    start_pos = sequence_positions[0]  # Get the starting position from the sequence
                    sequence_positions = sequence_positions[1:]  # Remove the starting position from the sequence

                if sequence_positions:
                    next_position = sequence_positions[0]  # Get the next position from the sequence
                    sequence_positions = sequence_positions[1:]  # Remove the next position from the sequence
                    move_truck(canvas, start_pos, next_position, character_images, map_image, map_scale)

                    canvas.after(2000, move_to_next_position, next_position,
                                 sequence_positions)  # Wait 2 seconds before moving to the next position

            move_to_next_position(None, sequence_positions)  # Start the movement sequence

        left_frame = tk.Frame(self)
        left_frame.pack(side=tk.LEFT, padx=20, pady=0)

        sequence_label = tk.Label(left_frame, text="Enter sequence (comma-separated):")
        sequence_label.pack()

        input_sequence_entry = tk.Entry(left_frame)
        input_sequence_entry.pack()

        start_sequence_button = tk.Button(left_frame, text="Start Sequence", command=start_movement)
        start_sequence_button.pack()

        reset_button = tk.Button(left_frame, text="Reset Simulation", command=reset_simulation)
        reset_button.pack()

        right_frame = tk.Frame(self)
        right_frame.pack(side=tk.RIGHT, padx=20, pady=0)

        canvas_width = 960
        canvas_height = 500

        map_scale = 50
        map_image_path = "C:\\Users\\admin\\PycharmProjects\\Rice-Distribution-Simulation\\simulation\\world_map(small).png"
        map_image = tk.PhotoImage(file=map_image_path)

        canvas = tk.Canvas(right_frame, width=canvas_width, height=canvas_height)
        canvas.create_image(0, 0, anchor="nw", image=map_image)
        canvas.pack()


class SimulationResultPage(tk.Frame):
    def __init__(self, parent, controller, themename="superhero", **kwargs):
        tk.Frame.__init__(self, parent)
        self.style = ttk.Style(theme=themename)
        self.title = "Simulation Results"
        colors = self.style.colors
        label = tk.Label(self, text="Simulation Results", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, bootstyle="info-outline", text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack(side=tk.TOP, anchor="nw", padx=10, pady=10)

        coldata = [
            {"text": "Distributor", "stretch": False},
            "Number of Helper", "Destination",
            {"text": "Delivery Time", "stretch": False},
        ]

        rowdata = [
            ('A123', 'IzzyCo', 12),

        ]

        dt = Tableview(
            master=self,
            coldata=coldata,
            rowdata=rowdata,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(colors.light, None),
        )
        dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # # Table headers
        # headers = ["Distributor", "Number of Helper", "Destination", "Delivery Time"]

        # # Create treeview (table) widget
        # self.tree = ttk.Treeview(self, columns=headers, show="headings")

    #     # Set column headings
    #     for header in headers:
    #         self.tree.heading(header, text=header)
    #         self.tree.column(header, anchor="center")
    #
    #     self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    #
    # def update_table(self, distributor, num_helper, destination, delivery_time):
    #     # Insert data into the table
    #     self.tree.insert("", "end", values=(distributor, num_helper, destination, delivery_time))


if __name__ == "__main__":
    app = SeaofBTCapp()
    app.mainloop()
