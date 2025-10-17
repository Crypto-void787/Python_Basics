'''Gettting continue statement '''

print("Straight loop")
i = 1

while i <= 5 : 
    if i == 3 :
         i += 1 
         continue 
    
    print(i) 
    i += 1 

print('Loop Ended\n')


print("\nReverse loop")
j = 5

while j >= 1 : 
    if j == 3 :
         j -= 1 
         continue 
    
    print(j) 
    j -= 1 

print('Loop Ended\n')

''' Getting break statement '''

k = 5 
while k >= 1 :
     if(k == 2):
          break 
     
     print(k)
     k -= 1 