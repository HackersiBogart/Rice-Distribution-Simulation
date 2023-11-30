import random


class DeliverySimulation:
    def __init__(self, starting_points, destinations, distance_matrix):
        self.starting_points = starting_points
        self.destinations = destinations
        self.distance_matrix = distance_matrix
        self.speed = 50  # Speed in km/h (you can change this based on your scenario)

    def calculate_delivery_time(self, start_point, destination):
        # Retrieve distance from the distance matrix
        distance = self.distance_matrix[self.starting_points.index(start_point)][self.destinations.index(destination)]

        # Calculate delivery time using the formula: time = distance / speed
        delivery_time = distance / self.speed
        return delivery_time

    def get_delivery_times(self, start_point, destinations):
        total_time = 0
        individual_times = {}
        for destination in destinations:
            time = self.calculate_delivery_time(start_point, destination)
            total_time += time
            individual_times[destination] = time
        return total_time, individual_times

    def overall_delivery_time(self, starting_point, destinations):
        total_time = 0
        for destination in destinations:
            total_time += self.calculate_delivery_time(starting_point, destination)
        return total_time


# Example usage:
starting_points = ["A", "B", "C"]
destinations = [f"D{i}" for i in range(1, 15)]

# Define the distance matrix (replace with actual distances)
distance_matrix = [
    [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
    [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155],
    [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]
]

simulation = DeliverySimulation(starting_points, destinations, distance_matrix)

# User input for starting point and destinations
start_point_input = input("Enter the starting point (A, B, C): ")
destination_input = input("Enter the destinations (D1, D2, ...): ")

# Ensure valid input
if start_point_input in starting_points:
    destination_list = [dest.strip() for dest in destination_input.split(',')]
    valid_destinations = all(dest in destinations for dest in destination_list)

    if valid_destinations:
        total_delivery_time, individual_delivery_times = simulation.get_delivery_times(start_point_input,
                                                                                       destination_list)
        overall_time = simulation.overall_delivery_time(start_point_input, destination_list)

        print(
            f"\nTotal Delivery Time from {start_point_input} to {', '.join(destination_list)}: {total_delivery_time:.2f} hours")
        print(f"Overall Delivery Time: {overall_time:.2f} hours")

        print("\nIndividual Delivery Times:")
        for destination, time in individual_delivery_times.items():
            print(f"{destination}: {time:.2f} hours")
    else:
        print("\nInvalid destination input. Please enter valid destinations.")
else:
    print("\nInvalid starting point. Please enter a valid starting point.")
