class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("Ford", "Mustang", 1969)
    car3 = Car("Tesla", "Model 3", 2024)

    print(car1.get_info())
    print(car2.get_info())
    print(car3.get_info())