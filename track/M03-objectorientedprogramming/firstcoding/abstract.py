# from abc import abstractmethod , ABC

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass
    
# # Abstract child class 
# class Car(Vehicle):
#     def start(self):
#         print("Car starts")
    
#     @abstractmethod
#     def stop(self):
#         pass

# # concrete method
# class sedan(Car):
#     def stop(self):
#         print("sedan Stops")

# s = sedan()
# s.start()
# s.stop()

### To find solution for this we use abstraction
class Vehicle:
    def start(self):
        print("Vehicle starts")

    def stop(self):
        print("Vehicle stops")
    
# child class override implimentation
class Car(Vehicle):
    def start(self):
        print("Car starts")
    
c = Car()
c.start()
c.stop()