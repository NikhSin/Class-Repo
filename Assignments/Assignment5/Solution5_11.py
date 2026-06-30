#Write a program to check whether a given key exists in the dictionary 
d = {1: 100, 2: 200, 3: 300} 

p=int(input("Enter the key to check even the key exist or not: "))
d = {1: 100, 2: 200, 3: 300} 

p=int(input("Enter the key to check even the key exist or not: "))

for key,value in d.items():
    if p==key:
        print("Exist")