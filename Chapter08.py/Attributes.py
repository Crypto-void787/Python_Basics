''' Attributes refer to any variable / data 
     we have two types of attribute: 
      1- Class attribute ( these are common for all class objects ) 
      2- Instance/Object attribute (like name of every student is different ) '''

class Student : 
    
    def __init__ (self) :
       print(self)

    def __init__ (self, name, Roll_no) :
        self.name = name 
        self.Roll_no = Roll_no
        print("Adding new student!")


s1 = Student('Ania' , 56)

print(s1.name , s1.Roll_no)