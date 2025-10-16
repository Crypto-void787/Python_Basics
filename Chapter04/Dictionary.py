# Dictionary used to store data values in key:value pairs 

''' dict = {
'name' : 'Ania' ,
'cgpa' : 3.98 ,
'marks' : [25, 24, 23, 24.5]
} 
    Dictionary syntax'''

# Sm properties 
''' 1- unordered (doesn't owe any index)
    2- Mutable 
    3- Duplication not allowed  '''

Student = {
     'Name' : 'Zara' ,
     'CGPA' : 3.87 ,
     'Country' : 'UK' ,
     'Subjects' : ['Python' , 'C++' , 'JavaScript' ] ,
     'Marks' : (24 , 25 , 23, 24.5) ,
     12 : (24 , 25 , 23, 24.5)
}
 
'''The datatype of key should be immmutable 
   like string, tuple, float, int. 
   It cant be mutable datatype key like list'''

print("Printing dictionary:\n" ,Student)
print("Type of Dictionary:", type(Student))

# Altering any key value in our di0ctionary 
Student['Name'] = 'Ania'
Student['Country'] = 'Dubai'
print(Student)

# Getting individual values of different keys 
print("\nGetting individual values\n" , Student['Name'] , "\n" , Student[12] , "\n" , Student['Subjects'] , "\n" , Student['CGPA'])

# Adding another key value pair 
Student['Disability'] = None

''' Right here we did ASSIGNMENT but
     in actual dictionary uses : (colon)'''

print("Printing dictionary:\n" ,Student)


''' let's create empty dictionary '''
Empty_dic = {

}
print("Printing Null dictionary:" , Empty_dic)

'''Taking advantage of mutability of dictionary datatype'''
Empty_dic['Hey'] = 'Im null'
Empty_dic[7] = 7
print("Printing Null dictionary after adding key:value :\n" , Empty_dic)
