
''' Let's play with nested dictionary '''

Student = {
    'Name' : 'Anaya' , 
    'Grade' : 7 , 
    'Subjects' : {
        'Mathametics' : 49.9 ,
        'German' : 45 
    } , 
    'CGPA' : 3.87
}

print("Student dictionary:\n" , Student)
print( "\nAccessing nested dictionary named as Subject:\n",Student['Subjects'])
# print("German" , Student['German'])
print( "\nAccessing nested dictionary's keys:",Student['Subjects']['German'])


print( "Name before:", Student['Name'])

Student['Name'] = 'Zoobi' #Altered 
print( "Name After:", Student['Name'])

Student['Disability'] = None

print("\nStudent dictionary:\n" , Student)
