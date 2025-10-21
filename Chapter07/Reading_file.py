f = open("demo.txt" , "+r")
data = f.read(9) # to read particular set of character 
print(data)
f.close()

''' Also can read line by line using readline()'''
print("\nReading line by line:")
f = open("demo.txt" , "r")
line1 = f.readline() 
print(line1)

line2 = f.readline() 
print(line2)

f.close()


'''simple printing '''

f = open("demo.txt" , 'r')
data = f.read()
print(data)

''' Reading data once aint reading it anymore line by line 
     we have to re run the file '''
 
line1 = f.readline() # ain't printing the line anymore  
print(line1)

line2 = f.readline()  # not printing the line anymore 
print(line2)

f.close()
