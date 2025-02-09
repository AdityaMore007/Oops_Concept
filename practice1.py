## Create Student Class that takes brand & marks of 3 subjects as arguments in constructor. Then create a method to print the Average.


# class Student:
#     def __init__(self,brand,marks):
#         self.brand = brand
#         self.marks = marks
        
        
#     def get_avg(self):
#         sum = 0
#         for value in self.marks:
#             sum+=value
#         print("hi",self.brand, "your Avg Score is:",sum/3)
        
# s1 = Student('Tony Stark' , [99,98,95])
# s1.get_avg()

# s1.brand = "Captain America"
# s1.get_avg()

# class Student:
#     def __init__(self,brand):
#         self.brand = brand
        
# s1 = Student('Aditya')
# print(s1.brand)
# del s1.brand
# print(s1.brand)


# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
#     def reset_pass(self):
#         print(self.__acc_pass)
        
        
# acc1 = Account("12345","abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass())


# class Person:
#     __name = "Anonymous"
    
#     def __hello(self):
#         print("hello User!!")
        
#     def welcome(self):
#         self.__hello()
    
# p1 = Person()

# # print(p1.__hello())
# print(p1.welcome()) 

# Inheritance

class Car:
    color = "balck"
    
    @staticmethod
    def start():
        print("Car Started..")
        
    @staticmethod
    def stop():
        print("Car Stopped..")
        
class ToyotaCar(Car):
       def __init__(self,brand):
            self.brand = brand
            
# car1 = ToyotaCar("Fortuner")
# Car2 = ToyotaCar("Legender")

# print(car1.brand)
# print(car1.start())

# print(car1.color)

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
        
car1 = Fortuner("Diesel")
car1.start()
