''' creating a new file "Practice.txt using python, and add following data 
    Hi everyone
    we are learning file I/O 
    using Java
    I like programming in Java. 
    
    
     Search if the word learning exist in the file or not '''


def Check_for_word(word) :
     with open("Chapter07/Files/Practice.txt" , "r+") as w :
         f = w.read()

         if (f.find(word) != -1) :
             print("Found!") 
         else:
             print("Not found")     



Check_for_word("learning")