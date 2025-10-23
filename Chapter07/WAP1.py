''' creating a new file "Practice.txt using python, and add following data 
    Hi everyone
    we are learning file I/O 
    using Java
    I like programming in Java.  '''



with open("Chapter07/Files/Practice.txt" , "a+") as f : 
    f.write("Hi everyone")
    f.write("\nWe are learning File I/O")
    f.write("\nusing Java")
    f.write("\nI like programming in Java.")
    f.seek(0)
    print(f.read())

    ''' It will close itself by its own '''