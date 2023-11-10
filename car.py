class Car:

    def init(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def update_mileage(self, mileage):
        self.mileage = mileage

    def print_info(self):
        print(f"Марка: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.year}\nПробег: {self.mileage}")
