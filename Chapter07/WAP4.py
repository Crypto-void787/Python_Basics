''' in which line of the file having the learning word occur first 
print -1 if word not found '''

def check_for_line(word) :
     data = True 
     line_no = 1
     with open("Chapter07/Files/Practice.txt" , "r+") as f :          
          while data: 
               data = f.readline()
               if(word in data) :
                    print(line_no)
                    return
               line_no += 1
          return(-1)

                


check_for_line("learning")                  

''' We can check anyother word via this  ''' 


