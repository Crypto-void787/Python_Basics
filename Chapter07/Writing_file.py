w = open("writing.txt" , 'w')
output = w.write("M learning python")





w = open("writing.txt" , "a") #append mode 
w.write("\nM gonna study DBMS after this!")
w.close()


w = open("writing.txt" , 'r')
Reading = w.read()
print(Reading) 
w.close() 

''' if a certain file ain't exist n we r opening it via 
    w(writing mode) or a(append mode) they'll create it 
    by themselves '''



''' But what if we have to do both reading n writing simultaneously 
   there are multiple ways to do it '''