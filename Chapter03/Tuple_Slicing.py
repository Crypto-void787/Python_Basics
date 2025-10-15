''' Same rule as normal list slicing '''
''' But in tuple intead of square bracket use paranthesis'''

Student = ("Adrien", 53 , 3.98)

print( "Tuple: ", Student)

print("\nPositive slicing!")
print("Slicing as str(Student[0 : 3]): " + str(Student[0 : 3]))
print("Slicing as str(Student[1 : 3]): " + str(Student[1 : 3]))
print("Slicing as str(Student[0 : 2]): " + str(Student[0 : 2]))
print("Slicing as str(Student[0 : 1]): " + str(Student[0 : 1]))

print("\nNegative slicing!")

print("Slicing as str(Student[-3 : ]): " + str(Student[-3 : ]))
print("Slicing as str(Student[-2 : ]): " + str(Student[-2 : ]))
print("Slicing as str(Student[-3 : -1]): " + str(Student[-3 : -1]))
print("Slicing as str(Student[-3 : -2]): " + str(Student[-3 : -2]))


''' Simple as fuck dude '''