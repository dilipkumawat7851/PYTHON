f = open('data.txt','r+')

#read the entire file
data = f.readlines()

#print the data 
print(data)

#write to the file 
f.write("\nThis is a new line added to the file\n")   
#close the file
f.close()

