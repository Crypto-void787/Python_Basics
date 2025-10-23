''' creating a new file "Practice.txt using python, and add following data 
    Hi everyone
    we are learning file I/O 
    using Java
    I like programming in Java. 
     
      
       Repalcing all occurence of jave with python  '''

import os

with open("Chapter07/Files/Practice.txt" , "r") as f : 
    data = f.read()
    new_data = data.replace("Java" , "Python")
    print(new_data)

with open("Chapter07/Files/Practice.txt" , "w") as f : 
    f.write(new_data)

    #overwrite the data to make it python in actuall file 