## Methods: Methods are the functions that belongs to the Objects.

class Student:
    college_name = "ABC College"
    # name = "Anonymous"
    # # deafult constructor
    # def __init__(self):
    #     pass
   
    # parametrized constructors 
    def __init__(self,name,marks):
        
        self.name = name
        self.marks = marks
        print("Creting new student!!")
        
        
    def Welcome(self):
        print("Welcome Student:",self.name)
        
    def get_marks(self):
        return self.marks
        
s1 = Student("Karan",97)
s1.Welcome()
print(s1.get_marks())