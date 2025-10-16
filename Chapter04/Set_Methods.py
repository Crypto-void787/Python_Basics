''' like others set also possess methods: 
       - add() # add you dude `
       - remove() # remove the given ele 
       - clear() # empties the set
       - pop()  #removes random value 
       - union()
       - intersection()'''

print("add() Method!")
A = set()  # an empty set 
''' Let's add ele in it '''
print("Before Add(): " + str(A))

A.add(1)
A.add(2)
A.add(3)
A.add(2)
A.add(4)
A.add(('T','Y'))

print("After Add(): " + str(A))


print("\nremove() Method!")
print("Before remove(): " + str(A))

A.remove(3)

print("After remove(): " + str(A))

print("\npop() Method!")
print("Before pop(): " + str(A))

A.pop()

print("After pop(): " + str(A))

print("\nclear() Method!")
print("Before clear(): " + str(A))
print("Before clear(): " + str(len(A)))

A.clear()

print("After clear(): " + str(A))
print("After clear(): " + str(len(A)))


s1 = {1, 2, 'A'}
s2 = { 3, 1, 'B'}
print("\n\nSet 1: " + str(s1) + " | Set 2: " + str(s2))

print("\nUnion() Method!")
s = s1.union(s2)
print("Union of set 1 and set 2:" + str(s)) 

print("\nInteresection() Method!")
s = s1.intersection(s2)
print("Union of set 1 and set 2:" + str(s))
