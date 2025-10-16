
# storing the word meaning in dictionary 

Dictionary = { 
     "Table" : ["a piece of furniture" , "list os facts and figure"] , 
     "cat" : "a smol n goofy animal " 
}

print( "Table: " + str(Dictionary.get("Table")))
print( "cat: " + str(Dictionary.get("cat")))
print("Dictionary: \n" + str(list(Dictionary.items())))
