#Write a program to remove duplicate values from a dictionary.
d1={1:'Nikhil',2:'Prabhat',3:'Rashid',4:'Priyanka',5:'Nikhil',6:'Prabhat'}
b="" 
for i,(keys,value) in enumerate(d1.items()):
    if value not in b:
        b+=value
print(b)
