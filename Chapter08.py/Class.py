''' Class is blueprint for creating objects or instance '''

# creating class 
class Student :

    def __init__(self):  # Default Construcutor
         pass 

    def __init__(self, name , marks ):  #Parametrized Construcutor
         self.name = name
         self.marks = marks
         print("\nAdding new student in database...")



# Creating instance 
s1 = Student("Ania" , 99)
print(s1.name , s1.marks)    

print(s1)  # getting location of this object storred in our device 

''' Self parameter:  is reference to current instance os class, n is used
    to access variables that belong to that class '''

''' constructor: Always call when class being initiated  '''

s2 = Student('Lii' , 87)
print(s2.name , s2.marks)
print(s2)

