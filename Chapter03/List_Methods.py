''' Methods are specific for each datatype 
    Like we studied sm specific methods for string before like 
      - capatilize() #capatilize the first letter of the string 
      - find() #find any letter in that string 
      - count() #count any letter or word in string 
      - endswith() # return true if string end with the given value 
      - replace() # Replace first one with the second letter or word '''

''' So same we gonna study sm list methods fr
     These are: 
        - append() #add one element at the end 
        - sort() #Sort out the orer of list 
        - reverse() #reverse the list 
        - insert() #insert element at the index 
        - sort(reverse = True) # sort the list in descending order 
        - remove() # remove first occurence of ele in list
        - pop() # remove element at index this'''

# lets dive in 'em 

lst = [23, 24.5, 25, 21, 20, 22]

print("List:" , lst )

print("\nappend method!")
lst.append(19)
print("appended list:" , lst )
lst.append(17)
print("Ultra appended list:" , lst )


print("\nsort method!")
lst.sort()
print("Sorted list:" , lst)


print("\nList sorted in revese order!")
lst.sort(reverse = True)
print( "List sorted out in descensding/reverse order:" , lst)

print("\nReversed list!")
lst.reverse()
print("Reversed list:" , lst)

''' AS list is mutable so next method always 
     folloeing the previous alterations made 
       by other methods in the list !'''

print("\nInsert Method!")
lst.insert(1, 22) 
''' Inserting 15 at index 1 '''
print("Insert method over list:" , lst)

print("\nRemove method!")
lst.remove(22)
""" Removing the first occurence of number 22 """
print("Removed:" , lst)

print("\nPop Method!")
lst.pop(3)
""" Remove the number at index 3"""
print("pop:" , lst)