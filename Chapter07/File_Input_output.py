''' Python can be used to perform various operations on a file (read and write)
 
   Types of file : 
         1- text file (.txt | .docx | .log etc)
         2- Binary files (.mp4 | .mov | .pnj | .jpeg etc)'''


''' RAM -> all varaible create here for short time 
    To keep for long term we store all of code in file format '''

''' Open, read & close file 
           f = open("file_name" , "mode" )
                                   by default its read mode 
                    -> .txt        r: read mode 
                    -> .docx       w : write mode '''


''' data = f.read()
    f.close()   '''


f = open("demo.txt" , "a")
data = f.write("wzup")
f.close()

f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()


""" Operations over file :
           r for read 
           w for overwrite 
           x for creating a new file 
           a for writing n appending that at the end 
           b for binary mode
           t for text mode
           + open a disk file for updating and writing """



