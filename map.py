import random
import matplotlib.pyplot as plt


class Distributor:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Destination:
    def __init__(self, name, location, rice_quantity):
        self.name = name
        self.location = location
        self.rice_quantity = rice_quantity


def calculate_delivery_time(distributor, destinations):
    total_distance = sum(abs(distributor.location - dest.location) for dest in destinations)
    delivery_time = total_distance / 10
    return delivery_time


def plot_map(distributors, destinations, selected_distributor, selected_destinations, delivery_time):
    plt.figure(figsize=(10, 6))

    # Plot distributors
    for distributor in distributors:
        plt.scatter(distributor.location, 0, marker='^', label=distributor.name, s=100)

    # Plot destinations
    for dest in destinations:
        plt.scatter(dest.location, 0, marker='o', label=f"{dest.name} ({dest.rice_quantity} kg)", s=dest.rice_quantity)

    # Highlight selected distributor
    plt.scatter(selected_distributor.location, 0, marker='s', color='red', label='Selected Distributor', s=150)

    # Highlight selected destinations
    for dest in selected_destinations:
        plt.scatter(dest.location, 0, marker='*', color='orange', label=f"Selected {dest.name}", s=dest.rice_quantity)

    plt.xlabel('Location')
    plt.title('Rice Distribution Map')
    plt.legend()

    # Display delivery time
    plt.text(5, -5, f"Estimated Delivery Time: {delivery_time:.2f} hours", ha='center', va='center', fontsize=12,
             color='blue')

    plt.show()


def main():
    distributor1 = Distributor("Distributor 1", 0)
    distributor2 = Distributor("Distributor 2", 5)
    distributor3 = Distributor("Distributor 3", 10)
    distributors = [distributor1, distributor2, distributor3]

    destinations = [
        Destination("Dest 1", 2, 100),
        Destination("Dest 2", 4, 50),
        Destination("Dest 3", 6, 75),
        Destination("Dest 4", 8, 120),
        # ... add more destinations
    ]

    selected_distributor = random.choice(distributors)
    selected_destinations = random.sample(destinations, k=random.randint(1, len(destinations)))

    print(f"Selected Distributor: {selected_distributor.name}")
    print("Selected Destinations:")
    for dest in selected_destinations:
        print(f"- {dest.name} ({dest.rice_quantity} kg)")

    delivery_time = calculate_delivery_time(selected_distributor, selected_destinations)
    print(f"Estimated Delivery Time: {delivery_time} hours")

    plot_map(distributors, destinations, selected_distributor, selected_destinations, delivery_time)

if __name__ == "__main__":
    main()
