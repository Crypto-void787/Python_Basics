''' Class methods as function but in class using class attributes '''

class Greeting:
    def __init__ (self, name):
        self.name = name 

    def Greeting(self):
        print(f"Good morning, {self.name}")    


class Numbers: 
    def __init__ (self, num1 , num2):
        self.num1 = num1  #referes the instance's attribute to the original onme  
        self.num2 = num2 

    def add(self) :
        print(f"Sum of {self.num1} and {self.num2} is : {self.num1 + self.num2}")   



G1 = Greeting("Irza") 
G1.Greeting() 


N1 = Numbers(3, 4)
N1.add()