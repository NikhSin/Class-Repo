# Write a program to count how many values are greater than 50 in a dictionary. 
d={1:23,2:43,3:56,4:76,5:87}
count=0
for keys,value in d.items():
    if value>50:
        count+=1
print(count)        

