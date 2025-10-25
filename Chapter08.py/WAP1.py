''' Taking name and marks of three sub as argumnet and then a method to print out 
    the average! '''
# nonstatic methods 

''' 1st way outta alot of ways : '''

class Student:
    def __init__ (self , name , marks1 , marks2 , marks3 ) :
        self.name = name 
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average_marks(self) :
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print(f"Average of your marks is: {str(avg)} ") 


''' 2nd way '''

class Students: 
    def __init__ (self, name , marks) :
        self.name = name 
        self.marks = marks 

    def Avg_marks(self):
         sum = 0 
         for val in self.marks:
             sum += val 
         print(f"Average of {self.name} is {str(sum/3)}")   


s1 = Student('Zoobia' , 34 , 36, 37)
s1.average_marks()

s3 = Students('Zooi' , [34 , 36, 37])
s3.Avg_marks()