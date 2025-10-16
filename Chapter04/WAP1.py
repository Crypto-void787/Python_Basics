# Finding exact class room requirement if one classroom require for aone sub 
 
sub1 = {'python' , 'java' , 'C++' , 'python' , 'js'}
sub2 = {'java' , 'C++' , 'java' , 'python' , 'C'}

print("Subjects: \n", sub1 , "\n" , sub2 )


classroom = sub1.union(sub2)

print("\nClassroom needed: " + str(len(classroom)))