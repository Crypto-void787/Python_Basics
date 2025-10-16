'''ALERT: Set are mutable but the elements of set are totally immutable '''

''' SET: unordered(no idexing), unique value , duplicate gonna ignore in set hmph🤧
   Muteable: 
       - List = [ ]
       - Dictionary = { }
   Immutable:
        - string
        - tuple = ()  
         
          so in set we can store jus unique values like str, int, float, tuple inshort list n dictionary 
            can never store in set  '''

Z = {1, 3, 'hello' , 2, 3 , 'hello' , 1}
print(Z)  # it will remove duplicate values and print only unique values
print(type(Z))

''' Fact: 
         set sort out itself by its own '''

# Empty set syntax 

A = {}
''' empty dictionary not a set 
In fact if we print out its type it gonnna be dictionary '''
print("A: " + str(A) + ", Type: " , str(type(A)))

A = set()  # This is empty set syntax 
print("A: " + str(A) + ", Type: " , str(type(A)))
