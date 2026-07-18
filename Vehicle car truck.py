class Vehicle:
    def __init__(self, make, model, year, fuel_capacity):
        self.make = make; self.model = model
        self.year = year; self._fuel  = fuel_capacity
    def start_engine(self): print(f'{self.make} {self.model} engine started')
    def refuel(self, litres):
        self._fuel += litres
        print(f'Refuelled {litres}L. Total: {self._fuel}L')
 
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_cap, num_doors):
        super().__init__(make, model, year, fuel_cap)
        self.doors = num_doors
    def honk(self): print('Beep beep!')
 
class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_cap, payload_tonnes):
        super().__init__(make, model, year, fuel_cap)
        self.payload = payload_tonnes
    def load_cargo(self, weight):
        if weight > self.payload: print('Overloaded!')
        else: print(f'Loaded {weight}T. Payload used: {weight}/{self.payload}T')
