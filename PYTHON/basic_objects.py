a = [1,True,3.3,'it cloud',5] # this is a list & it  contain ANTHING

b = [1,3,4,5] 

c = [1,2,3,4,5,6,7,8,9,10] # this is a list of 10 elements

result = c[1:7]

a. append(c) # this is how we can add new element in list

print(b[3])
print(a)
print(result)

#tuple

d= (1,2,3,4,5) # this is a tuple & it is immutable
#d[0] = 10 # this will give error because tuple is immutable
print(d)

# set
e = {1,2,3,4,5} # this is a set & it is unordered collection of unique elements 
e.add(6) # this is how we can add new element in set
print(e)

#dictionary
f = {'name':'John','age':30,'city':'New York'} # this is a dictionary & it is a collection of key-value pairs
print(f['name']) # this is how we can access value in dictionary using key
f['age'] = 31 # this is how we can update value in dictionary using key
print(f)

