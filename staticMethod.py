## Static Methods: Methods that don't use the self Paramter (work at class level)

# Decorator allows us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod   
    def hello():
        print("Hello Everybody, How are you all..") 
     
    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum+=value
        print("hi",self.name, "your Avg Score is:",sum/3)
        
s1 = Student('Tony Stark' , [99,98,95])
s1.get_avg()

s1.name = "Captain America"
s1.get_avg()

s1.hello()