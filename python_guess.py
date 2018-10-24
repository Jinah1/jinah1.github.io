import random

print("Here is a random number between 1-100:")
for x in range(1):
  print ("The number is: ", random.randint(1,101))
print("Now you are going to guess a number between 1-10. You have 5 tries.")
gameExit = False
acc = 4 
while (gameExit == False):
  x = int(input("Please guess: "))
  if (x==5):
    acc=5
    print("You win")
    gameExit = True
  else:
    print("Loser")
  if (acc == 4):
    print("You have 4 tries remaining")
  if (acc == 3):
    print("You have 3 tries remaining")
  if (acc == 2):
    print("You have 2 tries remaining")
  if (acc == 1):
    print("You have 1 try remaining")
  if (acc == 0):
    print("Game Over")
    gameExit = True
  acc = acc - 1