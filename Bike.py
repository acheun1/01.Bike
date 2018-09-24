#Bike
#2018 09 18
#Cheung Anthony

# Create a new class called Bike with the following properties/attributes:

# price
# max_speed
# miles
# Create 3 instances of the Bike class.
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

# What would you do to prevent the instance from having negative miles?

# Which methods can return self in order to allow chaining methods?

class Bike:
    miles=0
    ride=0
    reverse=0
    def __init__(self,price,max_speed,miles,ride,reverse):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles
        self.ride=ride
        self.reverse=reverse
    def displayInfo(self):
        self.total=int(self.miles+(self.ride*10)+(self.reverse*-5))
        if self.total <0:
            self.total=0
        print("price=" + str(self.price)+ ", Maximum speed="+ self.max_speed + ", Ride="+ str(self.ride) + ", Reverse="+ str(self.reverse) +", Total Miles="+str(self.total))
        return self
bike1=Bike(200,"25mph",1,3,1)
bike1=Bike(200,"25mph",1,2,2)
bike1=Bike(200,"25mph",1,0,3)
bike1.displayInfo()

# What would you do to prevent the instance from having negative miles?
# put a if statement so that when TOTAL miles is less then zero to TOTAL is zero

# Which methods can return self in order to allow chaining methods?
#bike1.price().max_speed().miles()
