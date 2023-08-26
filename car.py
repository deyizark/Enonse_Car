class Vehicle:
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Daily Rate: {self.daily_rate} dola")


class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_seats):
        super().__init__(make, model, year, daily_rate)
        self.num_seats = num_seats

    def display_info(self):
        super().display_info()
        print(f"Number of Seats: {self.num_seats}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, engine_type):
        super().__init__(make, model, year, daily_rate)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, frame_type):
        super().__init__(make, model, year, daily_rate)
        self.frame_type = frame_type

    def display_info(self):
        super().display_info()
        print(f"Frame Type: {self.frame_type}")


class Rental:
    def __init__(self, vehicle, rental_days):
        self.vehicle = vehicle
        self.rental_days = rental_days

    def calculate_total_cost(self):
        return round(self.vehicle.daily_rate * self.rental_days, 2)

    def display_receipt(self):
        print("Rental Receipt:")
        self.vehicle.display_info()
        total_cost = self.calculate_total_cost()
        print(f"Rental Days {self.rental_days}")
        print(f"Pri total : {total_cost} dola")

car = Car("Toyota", "Camry", 2023, 50, 5)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2023, 80, "V-twin")
bicycle = Bicycle("Trek", "FX", 2023, 15, "Hybrid")

car.display_info()
print()
motorcycle.display_info()
print()
bicycle.display_info()
print()
rental_car = Rental(car, 3)
rental_car.display_receipt()
print()
rental_motorcycle = Rental(motorcycle, 2)
rental_motorcycle.display_receipt()
print()
rental_bicycle = Rental(bicycle, 1)
rental_bicycle.display_receipt()