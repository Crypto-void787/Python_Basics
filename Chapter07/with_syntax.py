with open("Hello.txt" , "w+") as f : 
    f.write("Hello world!") 
    f.seek(0)
    # data = f.read()
    print(f.read())
    # f.close() # it gonna auto close the opened file 

with open("Bye.txt" , "a+") as w :
    w.write("See ya again, Goodbye! ")
    w.seek(0)
    print(w.read()) 
