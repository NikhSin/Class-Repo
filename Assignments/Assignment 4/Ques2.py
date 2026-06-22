#2. Write a Python program to display the odd and even elements from the list [10, 23, 11, 12, 33, 44, 2, 5, 6].
l1=[10, 23, 11, 12, 33, 44, 2, 5, 6]

# for i in range(len(l1)):
#     if l1[i]%2==0:
#         print(l1[i], "Even")
#     else:
#         print(l1[i],"Odd")

m=[f"{i} is Even" if i%2==0 else f"{i} is Odd" for i in l1]
print(m)