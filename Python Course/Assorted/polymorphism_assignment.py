#Parent class user to inheret from.
class Car:
    wheels = 4
    engine = True

    def information(self):
        msg = "\nThese are the attributes of a car.\nWheels: {}\nEngine: {}".format(self.wheels, self.engine)
        print(msg)
        


#First Child Class
class Sedan(Car):
    speed = 1
    color = "Red"
    four_wd = False

#A function calling the information from the parent & child classes.
    def information(self):
        msg = "\nThese are the attributes of a Sedan.\nWheels: {}\nEngine: {}\nSpeed: {}\nColor: {}\nFour Wheel Drive: {}".format(self.wheels, self.engine, self.speed, self.color, self.four_wd)
        print(msg)
        


#Second Child Class
class Truck(Car):
    speed = 0
    color = "Blue"
    four_wd = True

#A function calling the information from the parent & child classes.
    def information(self):
        msg = "\nThese are the attributes of a Truck.\nWheels: {}\nEngine: {}\nSpeed: {}\nColor: {}\nFour Wheel Drive: {}".format(self.wheels, self.engine, self.speed, self.color, self.four_wd)
        print(msg)
        


#Following code invokes the methods inside of each child class.
car = Car() #Variable for the parent class.
car.information()#This is calling the parent class function.

car1 = Sedan() #Variable for first child class 'Sedan' to pass.
car1.information() #This is calling the first child class function.

car2 = Truck() #Variable for the second child class 'Truck' to pass.
car2.information() #This is calling the second child class function.

