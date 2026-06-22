#3. Write a Python program to count the odd and even numbers in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].
l2=[10, 23, 11, 12, 33, 44, 2, 5, 6]
odd=0
even=0
# for i in range(len(l2)):
#     if l2[i]%2==0:
#         even+=1
#     else:
#         odd+=1
# print("Odd: ", odd)
# print("Even: ", even)

even=sum([1 for i in l2 if i%2==0])
odd=sum([1 for i in l2 if i%2!=0])
print(even)
print(odd)