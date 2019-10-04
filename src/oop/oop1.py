# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#Base Class for FlightVehicle, Starship, and GroundVehicle
class Vehicle():
    pass

class FlightVehicle(Vehicle):
    pass

#Base Class for Airplane that inherits from Vehicle
class Starship(FlightVehicle):
    pass

#Base Class for Car and Motorcycle that inherits from Base Class Vehicle
class GroundVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass