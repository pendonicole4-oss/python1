class Car:
    def __init__(self,colour,brand,seating_capacity,engine_type):
        self.colour=colour
        self.brand=brand
        self.seating_capacity=seating_capacity
        self.engine_type=engine_type
    def __str__(self):
        return f"A {self.colour} {self.brand}, with {self.seating_capacity} seats and uses {self.engine_type} as the engine type."


car1=Car("Black","Mercedes",5,"Diesel")
car2=Car("White","Lambogini",5,"Electric")
print(car1)
print(car2)
