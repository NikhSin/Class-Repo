#Write a program to find the greatest key in the dictionary 
player = {7: "Dhoni", 12: "Kohli", 9: "Rohit", 89: "Bumrah",99:"Nikhil"}
greatest=min(player)

for keys,value in player.items():
    if keys>greatest:
        greatest=keys
print(greatest)        