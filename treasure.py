import sys
print('''_                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')
print("Welcome to the treasure island")
print("Your mission is to find the treasure")
choice=input("You are at a cross road. Where do you want to go ? Type 'left' or 'right'\n").lower()
if choice=="left":
  print("You just died cause your choice wasn't RIGHT,HAHAHAHAAHAAHAAHHA")
  sys.exit()
else:
  print("You have reached a Lake.There is an island in The center of The lake\n")
choice=input("You want to wait for the Boat or Swim .Type 'boat' or 'swim'\n").lower()
if choice=="swim":
  print("You were just eaten by the crocodiles,NOM NOM")
  sys.exit()
else:
  print("You have reached the island unharmed\n")
choice=input("There are three doors on the island , RED , GREEN and BLUE .Type the one you choose\n").lower()
if(choice=="red"):
  print("You just won The treasureeee!!!")
  print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
elif(choice=="blue"):
  print("You just got thrown in Sea and eaten by Sharks:(")
  sys.exit()
elif(choice=="green"):
  print("You just got eaten by crocodiles :(")
  sys.exit()
