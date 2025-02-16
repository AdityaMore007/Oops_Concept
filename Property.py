class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    ## PROPERTY DECORATOR:  
    # def calPercentage(self):
    #     self.percentage = str((self.phy + self.math + self.chem)/3) +"%"
    
    @property
    def percentage(self):
        return str((self.phy + self.math + self.chem)/3) +"%"
        

        #percentage
student1 = Student(98,97,95) 
print(student1.percentage)   

student1.phy = 56
print(student1.percentage)   
         