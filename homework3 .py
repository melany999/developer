
from os import system
system("clear")

big_ship = int(input("Enter the coordinate of the big ship (1-10): "))
for x in range(1, 11):
    if x == big_ship:
        if x == 5:
            print("wWw", end="")
        else:
            print("W", end="")
    else:
        print("~", end="")
