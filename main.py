import simpy
import tkinter as tk
import random

coordinates = {
    "Daet": (10, 5),
    "banana": (15, 8),
    "orange": (20, 12),
}
class Market:
    def __init__(self, env, name, demand):
        self.env = env
        self.name = name
        self.demand = demand

class Vehicle:
    def __init__(self, env, market, quantity_rice):
        self.env = env
        self.market = market
        self.quantity_rice = quantity_rice
        self.action = env.process(self.run())

    def run(self):
        yield self.env.timeout(random.uniform(1, 5))  # Simulate travel time

        # Update market rice quantity after delivery
        self.market.demand -= self.quantity_rice

        print(f"Vehicle arrived at {self.market.name} at {self.env.now}")

def run_simulation(num_vehicles, num_markets, quantity_rice, traffic_factor, starting_locations, destinations):
    env = simpy.Environment()

    # Create the markets with demands
    market_demands = [random.randint(50, 200) for _ in range(num_markets)]
    markets = [Market(env, f"Market {i + 1}", market_demands[i]) for i in range(num_markets)]

    # Create the vehicles
    for _ in range(num_vehicles):
        market = random.choice(markets)
        Vehicle(env, market, quantity_rice)

    env.run(until=30)  # Set a simulation time limit (you can adjust this)

def start_simulation():
    try:
        num_vehicles = int(num_vehicles_entry.get())
        num_markets = int(num_markets_entry.get())
        quantity_rice = int(quantity_rice_entry.get())
        traffic_factor = float(traffic_factor_entry.get())

        run_simulation(num_vehicles, num_markets, quantity_rice, traffic_factor, starting_locations, destinations)
    except ValueError:
        status_label.config(text="Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Rice Distribution Simulation")

# Define starting_location and destinations after creating Tkinter root window
starting_locations = {
    "Happy Homes Pamorangon": "84 Kamagong St, Daet, 4600 Camarines Norte, Philippines",
    "Daet Central Market": "Daet, 4600 Camarines Norte, Philippines",
}
destinations = {
    "Daet, Bicol, Philippines": "Daet, Camarines Norte, Philippines"
}

# Create labels and input fields for parameters
num_vehicles_label = tk.Label(root, text="Number of Vehicles:")
num_vehicles_label.pack()
num_vehicles_entry = tk.Entry(root)
num_vehicles_entry.pack()

num_markets_label = tk.Label(root, text="Number of Markets:")
num_markets_label.pack()
num_markets_entry = tk.Entry(root)
num_markets_entry.pack()

quantity_rice_label = tk.Label(root, text="Quantity of Rice (per vehicle):")
quantity_rice_label.pack()
quantity_rice_entry = tk.Entry(root)
quantity_rice_entry.pack()

traffic_factor_label = tk.Label(root, text="Traffic Factor:")
traffic_factor_label.pack()
traffic_factor_entry = tk.Entry(root)
traffic_factor_entry.pack()

# Create dropdown menus for starting location and destination
starting_location_label = tk.Label(root, text="Starting Location:")
starting_location_label.pack()

starting_location_options = list(starting_locations.keys())
starting_location_var = tk.StringVar(root)
starting_location_var.set(starting_location_options[0])  # Set default value

starting_location_dropdown = tk.OptionMenu(root, starting_location_var, *starting_location_options)
starting_location_dropdown.pack()

destination_label = tk.Label(root, text="Destination:")
destination_label.pack()

destination_options = list(destinations.keys())
destination_var = tk.StringVar(root)
destination_var.set(destination_options[0])  # Set default value

destination_dropdown = tk.OptionMenu(root, destination_var, *destination_options)
destination_dropdown.pack()

# Create a button to start the simulation
start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
start_button.pack()

# Create a label to display the simulation status
status_label = tk.Label(root, text="Simulation Ready...")
status_label.pack()

# Keep the GUI running until it is closed
root.mainloop()