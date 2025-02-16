# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
#     def reset_pass(self):
#         print(self.__acc_pass)
        

# acc1 = Account("Aditya" , "12345")
# print(acc1.acc_no)
# print(acc1.reset_pass())

class Car:
    @staticmethod
    def start():
        print("Car Started")
        
    def stop():
        print("Car Stopped")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
        
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("prius")

# print(car1.name)

# print(Car.start())

print(car1.start())