# class A:
#     varA = "Welcome to Class A"
    
# class B:
#     varB = "Welcome to Class B"
    
# class C(A,B):
#     VarC = "Welcome to Class C"
    
# c1 = C()

# print(c1.varA)
# print(c1.varB)
# print(c1.VarC)


class Car:
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car Started..")
       
    @staticmethod    
    def stop():
        print("Car Stopped..")
    
class ToyotaCar(Car):
    def __init__(self, name,type):
        self.name = name
        super().__init__(type)
        super().start()
        
car1 = ToyotaCar("Priius" , "Electric")
print(car1.name)
print(car1.type)
# print(car1.start())

    