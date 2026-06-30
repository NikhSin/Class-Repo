#8. Write a program to extract alternate key-value pairs from the dictionary 
player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah"}
alt_pairs={}
for i, (keys,value) in enumerate(player.items()):
    if i%2==0:
         alt_pairs[keys]=value
print(alt_pairs)         