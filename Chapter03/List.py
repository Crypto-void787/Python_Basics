
# List are kind of array in any other language 
''' List used to store multiple variables within jus a single variable 
     but in list in python we can store multiple values of the diff type like str, int, float in a single variable'''

Marks = [34, 45, 67.6, 56, 98 ]

print(Marks)

print("\nMarks[0]: " + str(Marks[0]))
print("Marks[1]: " + str(Marks[1]))
print("Marks[2]: " + str(Marks[2]))
print("Marks[3]: " + str(Marks[3]))
print("Marks[4]: " + str(Marks[4]))

print( "Length of List Marks:" , len(Marks))

print("\n", type(Marks))

Person = ["Saad", 19 ]

print(Person)
print("\nName: " + Person[0])
print("Age: " + str(Person[1]))

print("Length of list Person:" , len(Person))


''' Mutable: Which can change 
     Immutable: which can't change '''

''' In python, Strings are immutable 
      meanwhile the list are mutable '''

''' As we knw list are mutable. 
    So using that rule we can change a
     string in list although its immutable
      but cz its in list so gonna apply the list rule over it  '''

# For instance

Person[0] = "Ania"

# Now printing that person list 
# Its altered 
print(Person)

''' Let's try to alter an individual string '''
str = "Hello!"
print(str[0])
# str[0] = "Y"   
''' Throwing a big horror error '''

print(str)  

''' But this same stuff is 
     completley possible on lists '''

''' Python ain't throwing error to
      alter the string from any list'''