print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇

print("You're at a crossroad.")
direction = input("Where do you want to go? Type 'left' or 'right': ").lower()

if direction == "left":
    print("You chose to go left.")
    print("You come across an old abandoned mansion.")
    print("The mansion looks eerie but you decide to enter.")
    print("Inside, you find three doors: one red, one yellow, and one blue.")
    door = input("Which door do you choose? 'red', 'yellow', or 'blue': ").lower()
    if door == "red":
        print("You enter a room filled with traps. Game over!")
    elif door == "yellow":
        print("You found a room with a treasure chest! You win!")
    elif door == "blue":
        print("You open the door and fall into a pit of spikes. Game over!")
    else:
        print("Invalid choice. Game over!")
elif direction == "right":
    print("You chose to go right.")
    print("You walk deeper into the forest and find a river.")
    print("You can 'swim' across or 'wait' for a bridge.")
    crossing = input("What do you do? 'swim' or 'wait': ").lower()
    if crossing == "wait":
        print("A bridge appears magically, and you cross it.")
        print("On the other side, you find a cave.")
        print("You enter the cave and find three tunnels: one dark, one dimly lit, and one brightly lit.")
        tunnel = input("Which tunnel do you choose? 'dark', 'dimly lit', or 'brightly lit': ").lower()
        if tunnel == "dark":
            print("You stumble into a nest of spiders. Game over!")
        elif tunnel == "dimly lit":
            print("You find yourself in a maze and can't find your way out. Game over!")
        elif tunnel == "brightly lit":
            print("You emerge from the tunnel into a chamber with the treasure! You win!")
        else:
            print("Invalid choice. Game over!")
    elif crossing == "swim":
        print("You are attacked by piranhas while swimming. Game over!")
    else:
        print("Invalid choice. Game over!")
else:
    print("Invalid choice. Game over!")
