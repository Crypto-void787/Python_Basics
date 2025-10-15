

str = "we're studying fuctions." 

# Returns True 
print(str.endswith("ns."))

#Returns False cuz it's not ending w Yo
print(str.endswith("Yo"))

''' This making it temporary capatilize '''
print(str.capitalize())
print("\n"+ str)

''' To make it permanent capatilize '''
str = str.capitalize()
print("\n"+ str)

''' will count letter i in  whole string '''
print(str.count("i"))

''' will replace the first letter with the second letter in whole string '''
print(str.replace("we're" , "we are"))

''' To find any word or letter in string 
    it'll print the index number of the given letter or word of the string'''
print(str.find("We"))
