#Write a program to find the maximum value in the dictionary 
marks = {"A": 85, "B": 90, "C": 75, "D": 95} 

max_val=None

for value in marks.items():
    if max_val is None or max_val<value:
        max_val=value
print(max_val)        