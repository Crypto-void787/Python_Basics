''' Getting factorial via loop '''

num = 5 
fact = 1 
i = 1 

while i <= num :
    fact *= i
    i += 1 

print("Factorial: " + str(fact))    