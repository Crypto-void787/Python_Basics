'''Dictionary's Method jus like of List, Tuples'''

''' 
- myDic.keys() #return all keys 
- myDic.values() #return all values 
- myDic.items() #returns all (key, vall) pairs as tuples
- myDic.get("key"") #return key accto value
- myDic.update(newDict) #insert specific items to the dictionaries  '''

tourism = {
    "country": "Japan",
    "famous_city": "Tokyo",
    "currency": "Yen",
    "visa_required": True,
    "popular_food": ["Sushi", "Ramen", "Takoyaki"]
}

print(tourism)

print("\nkeys() !\n" , tourism.keys()) #getting all keys 
print("\n" , list(tourism.keys())) # to get keys in list datatype rather then tuples
print(len(list(tourism.keys()))) # to get keys length
print( len(list(tourism))) # to get keys length

print("\nvalues() !\n" , tourism.values()) #getting all  values 
print("\ntuple:" , tourism.values()) 
print("list:" , list(tourism.values())) # to get values in list datatype rather then tuples
p = list(tourism.values())
print("indexing as its list now:" , p[0] , p[1])


print("\nitems() !" ) #return whole dictionary as tuple  
print("\ntuple:" , tourism.items()) 
print("list:" , list(tourism.items())) # to get values in list datatype rather then tuples
pairs =  list(tourism.items()) 
'''first convert into list datatype by type conversion and then one can access via indexing '''
print("pairs[0]:" , pairs[0])
print("pairs[3]" , pairs[3])


print("\nget() !\n" , tourism.get("popular_food")) # getting the valuees of the specific key 
# print("\nkeys() !\n" , tourism.update("lang")) 

print()