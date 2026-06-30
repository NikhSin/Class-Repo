#Write a program to convert two lists into a dictionary Example: keys = [1, 2, 3], values = ["a", "b", "c"]
keys = [1, 2, 3] 
values = ["a", "b", "c"] 

# for i in keys:
#     c={}
#     for j in values:
#         c[i]=j

# print(c)
res=zip(keys,values)
print(dict(res))