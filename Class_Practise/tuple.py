#-------Defination and property of tuple----------------#
#Tuple is a data structure in python used to store multiple data of different types with comma(,) in round braces.
#2.Immutable
#3. Support indexing slicing and ordered.
# 
# #--------Creation of tuple----------------#
# t1,t2,t3=(50,40,"nik")
# print(type(t1)
# print(t1)
# print(t2)
# print(t3)

# marks_tuple=(50,55,69,34,89)
# print(marks_tuple[-1])
# print(marks_tuple[::-1])

#mutability of tuple
# marks_tuple=(50,55,69,34,89)
# marks_tuple[2]=500
# print(marks_tuple)

#Traversing
# marks_tuple=(50,55,69,34,89)
# def marks_tuples(m):
#     new_tuple=[]
#     for i in marks_tuple:
#         if i>55:
#             new_tuple.append(i)
#     return new_tuple
# res=marks_tuples(marks_tuple)
# print(res)

##1 WAF to sum of indices

# marks_tuple=(50,55,69,34,89)
# def sum_of_indices(marks_tuple):
#     sum=0
#     for i in range(len(marks_tuple)):
#         sum+=i
#     return sum

# res=sum_of_indices(marks_tuple)
# print(res)

#Tuple Comprehension
# marks_tuple=(50,55,69,34,89)    

# def sum_of_indices(marks_tuple):
#     return sum([i for i in range(len(marks_tuple))])

# print(sum_of_indices(marks_tuple))


