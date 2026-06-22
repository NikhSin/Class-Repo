#1. Write a Python program to find the sum of all elements in the list [10, 20, 30, 40, 50].
num=[10,20,30,40,50]
sum=0
sum_num=[sum:=sum+i for i in num]
print(sum)