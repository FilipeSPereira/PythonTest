#class point():
#    def __init__(self, input1 , input2 ) :
#        self.x = input1
#        self.y= input2

#p = point(2, 8)
#print(p.x)
#print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity= capacity
        self.passangers=[]

        

    def add_passenger (self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)
    
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    Sucess = flight.add_passenger(person)
    if Sucess:
        print (f"Added {person} to flight sucessfully")
    else:
        print (f"No available seats for {person}")
