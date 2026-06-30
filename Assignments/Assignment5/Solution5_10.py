#Write a program to merge two dictionaries 
d1 = {1: "a", 2: "b"} 
d2 = {3: "c", 4: "d"} 

for i,(keys,value) in enumerate(d2.items()):
        d1[keys]=value
print(d1)        