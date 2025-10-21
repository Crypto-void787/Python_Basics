'''Calculating sum of first n natural number by recursive function'''

def sum(n):
    if n == 0 :
        return 0
    
    return sum(n-1) + n
    

print("Sum:" , sum(5))    