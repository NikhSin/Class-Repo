# Write a program to find all values that start with the letter ‘K’ 
player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah",88:"Kamal"} 
alt={}
for i, (key,value) in enumerate(player.items()):
    if value.startswith("K"):
        alt[key]=[value]
        
print(alt)        
