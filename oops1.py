class Student:
    college_name = "ABC College"
    name = "Anonymous"
    # deafult constructor
    def __init__(self):
        pass
        
        
    
    # parametrized constructors 
    def __init__(self,name,marks):
        
        self.name = name
        self.marks = marks
        print("Creting new student!!")
     
# obj att > class att #

s1 = Student("Karan",97)
print(s1.name)
# print(s1.name , s1.marks)

# s2 = Student("Arjun",98)
# print(s2.name , s2.marks)

print(Student.name)

# print(Student.college_name)

# print(s1.name)


# s2 = Student()
# print(s2.name)


# class Car:
#     color = "Blue"
#     brand = "BMW"
    
# car1 = Car()
# print(car1.color)
# print(car1.brand)

