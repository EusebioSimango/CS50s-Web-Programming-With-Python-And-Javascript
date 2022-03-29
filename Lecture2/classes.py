
# class Point():
#     def __init__(self, pointX, pointY) -> None:
#         self.x = pointX
#         self.y = pointY


# pointOne = Point(2, 8)
# print(pointOne.x)
# print(pointOne.y)

class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name) -> None:
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ["Harry", "Ron", "Hremione", "Ginny"]
for person in people:
    sucess = flight.add_passenger(person)
    if sucess:
        print(f"Added {person} to flight sucessfuly")
    else:
        print(f"No available seats for {person}") 