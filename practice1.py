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

class Student:
    def __init__(self,name):
        self.name = name
        
s1 = Student('Aditya')
print(s1.name)
del s1.name
print(s1.name)

## 2.31