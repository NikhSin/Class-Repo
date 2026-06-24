#1 Dictionary is a data structure in python used to store multiple data in key-value pairs.
#2.Ordered, Mutable.
#3.Indexed by key, not position.
#4. Key must be unique.
#5. value can be of any type.
#6 Used in fast lookup of data.

#Creation of Dictionary----------
# stu_profile={"aman":"noida", "rohit":"delhi", "sahil":"gurgaon"}
# print(stu_profile)
# stu_marks={("aman",90),("rohit",80)}
# print(stu_marks)

#Updating the value of a key in dictionary----------
# stu_profile={"aman":"noida", "rohit":"delhi", "sahil":"gurgaon"}
# stu_profile["aman"]="delhi"
# print(stu_profile)
# stu_marks={("aman",90),("rohit",80),("sahil",70),("aman",100)}
# sum=0
# for keys, values in stu_marks:
#     sum+=values

# print(sum)

# sum1=0
# for i,(keys, values) in enumerate(stu_marks):
#     sum1+=i
# print(sum1)

# #inbuilt-methods of dictionary----------
# stu_marks={("aman",90),("rohit",80),("sahil",70),("aman",100)}
# k=stu_marks.keys()
# v=stu_marks.values()
# print(k)

# students={"aman":90,"rohit":80,"sahil":70}
# k=students.items()
# print(k)    

# stu_marks={("aman",90),("rohit",80),("sahil",70),("aman",100)}
# res=stu_marks.get("aman","N/A")
# print(res)

#updating the dictionary----------update() method is used to update the dictionary with the elements from another dictionary object or from an iterable of key-value pairs.
# stu_marks={"aman":90,"rohit":80,"sahil":70,"aman":100}
# stu_marks_new={"kamal":90,"rohan":76,"fasal":80}

# stu_marks.update(stu_marks_new)
# print(stu_marks)
