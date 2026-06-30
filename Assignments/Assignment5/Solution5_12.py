#Write a program to find the minimum value in the dictionary 
marks = {"A": 85, "B": 90, "C": 75, "D": 95}

min_value=None
for value in marks.items():
    if min_value is None or value<min_value:
        min_value=value
        
print(min_value)