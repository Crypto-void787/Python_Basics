''' Finding factorial of n via function'''

'''Function definitions '''

def Factorial(a):
    fact = 1 
    for i in range(1, a+1):
        fact *= i

    print("Factorial via loop:", fact)
    return fact 


def Recursive_factorial(n) :
    if n == 1 or n == 0 : 
        return 1 
    else :
        return n * Recursive_factorial(n-1)
    


'''Fuction call '''
Factorial(5) 

print("Factorial via recurssive logic:" , Recursive_factorial(5))