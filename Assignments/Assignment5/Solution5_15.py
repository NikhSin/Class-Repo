#Write a program to remove a specific key (for example, key = 2) from the dictionary 
d = {1: 10, 2: 20, 3: 30} 
user=int(input("Enter key to remove:"))
c={}
for keys,value in d.items():
    if user!=keys:
        c[keys]=value
print(c)        