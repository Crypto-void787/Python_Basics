''' Tuples : same like list but w sm differences 
      - they've belonging with string as they also immutable 
      - unlike the list they written in () but works almost same as list except of mutability '''

# Let's dive in tuples! 


Tup = [3, 4, 5, 6, 7, 8, 9, 10]
print(Tup)
print(type(Tup))

print("\nSpot out the difference \n")

Tup = (3, 4, 5, 6, 7, 8, 9, 10)
print(Tup)

print(type(Tup))


#same as list we can access elemenets n do sm indexing 

print("\nindex[0]: " , Tup[0])
print("index[1]: " , Tup[1])
print("index[2]: " , Tup[2])
print("index[3]: " , Tup[3])
print("index[4]: " , Tup[4])
print("index[5]: " , Tup[5])

print("Len:" , len(Tup))

# but we can't alter the values of tuple like list 

''' 
      Tup[0] = 12 (Naaah)  
         as tuple immutable 
          same behaviour like a string '''


# lets make sm empty tup
print()

tup = ()
print("empty tuple:",tup)
print( "Len:", len(tup))
print(type(tup))

# single valued tuple ended by a single , $Rule 
print()

tuup = (2,)   
print("single value tuple:" , tuup )
print( "Len:", len(tuup))
print(type(tuup))

print()
tuup = (2.44)   # without comma single value tuple isn't a tuple anymore
print("tuup = (2.44): " , type(tuup))

print()
tuup = (2)   # without comma single value tuple isn't a tuple anymore
print("tuup = (2): " , type(tuup))

print()
tuup = ('Yo')   # without comma single value tuple isn't a tuple anymore
print("tuup = ('Yo): " , type(tuup))


''' To percieve it as single valued tuple
     its necessary to put comma at the end'''

