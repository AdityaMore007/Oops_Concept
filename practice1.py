## Create Student Class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the Average.


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
        
#     def get_avg(self):
#         sum = 0
#         for value in self.marks:
#             sum+=value
#         print("hi",self.name, "your Avg Score is:",sum/3)
        
# s1 = Student('Tony Stark' , [99,98,95])
# s1.get_avg()

# s1.name = "Captain America"
# s1.get_avg()

# class Student:
#     def __init__(self,name):
#         self.name = name
        
# s1 = Student('Aditya')
# print(s1.name)
# del s1.name
# print(s1.name)


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
       def __init__(self,name):
            self.name = name
            
car1 = ToyotaCar("Fortuner")
Car2 = ToyotaCar("Legender")

print(car1.name)
print(car1.start())

print(car1.color)

# 18.15