
''' M gonna demonstrate sm file access modes right here 
   but before that we must have to know what are they actually! 

      r -> read mode. We can read our file via this as f.read()

      r+ -> Read n write. By using this access mode we can perfom two operations.
           The first one is read() and the second one is write().File must already
           exist, otherwise error. You can read and write in it,but it doesn't erase
           what's already inside.
     
      w -> write file. With this we jus can write the file but can't read 
          it even for the testing purpose. if u wanna read must use the read access
          mode with it. It make file empty mean whatever we write its overwrite over the 
          first one. If the file we gonna write doesn't even exit, it create it n write it 
         
      w+ -> Opens file for both reading and writing (creates new file or overwrites existing one) 
            If file exists, it's completely erased first. If file doesn't exist, it's created automatically.
            U can read n write it normally but need to use seek(0) before reading it again sine the pointer 
            goes to end after writing. 
               
                  
      a -> appends the data, add it to end of file instead of overwriting it n if file doesn't exist this 
           a will create it n then we can write 
                             
      a+ -> Append + Read. Opens file for reading and appending.       '''



v = open("This.txt" , "w+")
w = v.write("\nIm a demo file") 
# rn the pointer is at the last of file so we have to seek(0) in order to print it from start 
v.seek(0) 
w = v.read()

# Lets use append access mode 
print(w)

''' This how w+ works lol'''

v = open("This.txt" , "a")
w = v.write("\nThis sentence is in via append access mode!")

v = open("This.txt" , "r+")
w = v.read()
print(w)

# Lets read it line by line 
''' As we know it literally gonna print nothing cz we already made it to print all file  before n now the pointer is at the end '''

line1 = v.readline()
print(line1)

line2 = v.readline()
print(line2)

v.close()




