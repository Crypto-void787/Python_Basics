# To prevent Redundant code we use functions 
# block of code that perform specific tasks

''' Function defination: 

 def func_name(param1, param2, ...) : 
       # same work
       return val   ''' 

''' Function call: 

funct_name(arg1, arg2 , ...)'''


def Sum(a , b) :
    return a + b
    # s = a + b
    # return s 

def Cal_Sum(a , b , c) :
    s = a + b + c
    print(s)
    return s
    


def Sqr(a): 
   return  (print(a ** 2))


Cal_Sum(3, 5, 4)

print(Sum(4,5))
Sqr(3)

''' This function ain't taking any input 
   n also not returning any output as return vaule '''

def Print_hello(): 
    print ("Hello")

output = Print_hello()
print(output) # gonna return none cz no output  


''' Let's create a function that calculates the avg of three numbers'''
def avg(a, b, c) :
    a = (a + b + c) / 3
    print("Average is: " + str(a))
    return a 

avg(1, 2, 3)


""" All is need to have proper indentation n we can use aall
    of the loops n conditional statements right in our functions  """

