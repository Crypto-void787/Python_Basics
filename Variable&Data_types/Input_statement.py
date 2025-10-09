
input("Enter your name: ") 
'''This will always take input as string datatype'''

name = input('Enter your name: ')
print(name)

age = int(input('Enter your age: '))
''' This gonna take input as the integer datatype cz we put type conversion there'''
print(age)

CGPA = float(input('Enter your CGPA: '))
'''This gonna take input as float datatype '''
print(CGPA, "Type of CGPA:", type(CGPA))



''' Type casting: Converting one datatype to another datatype'''

a = input("Any number: ")
print("You entered " + a + "!")
print("You entered " , a , "!")

''' The above two print statements are same but the first one 
is concatenation and the second one is just comma separation'''