#Write a program to find the total number of items in the dictionary 
d = {"apple": 5, "banana": 7, "cherry": 3} 

count=0

for i,(key,value) in enumerate(d.items()):
    count+=i

print(count)   