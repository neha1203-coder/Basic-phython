class car :
    def __init__(self,carname,brand ,colour ,price):
        self.carname=carname 
        self.brand=brand
        self.colour=colour
        self.price=price
    def drive(self):
        print(f"{self.carname} is ready to drive ")
    def stop(self):
        print(f"{self.carname} of brand {self.brand} is not ready to use ")

car1=car("first car "," bmw","red",2000)
print(car1.drive())