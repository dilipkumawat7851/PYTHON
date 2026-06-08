a = 10

b = int(input("Enter a number::"))

try:
    c = a/b
    print(c)
except ZeroDivisionError:   
    print("you cannot divide a number by zero") 
