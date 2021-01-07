#guess number game
import random
for x in range(1,11):
    guessnumber = int(input("plz enter your guess number 1 to 10:"))
    randomnumber = random.randint(1,10)
    if randomnumber == guessnumber:
      print("you have win the game")
    else:
     print("you have lost the game")
     print("random number is:" ,randomnumber)