#4. Create an empty dictionary called user_data. 
#Allow the user to enter key-value pairs until they choose to stop. 
#Print the final dictionary.




no_ofpairs=int(input("Enter the number pairs you want:"))
p={}

for i in range(no_ofpairs):
    key1=input("Enter the key: ")
    value1=input("Enter the value: ")
    p[key1]=value1
print(p)