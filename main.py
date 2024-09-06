from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print()
print("Select your move (R, P or S)")
print()
player_1 = input("Player 1 > ")
print()
player_2 = input("Player 2 > ")
print()
if player_1 == "R" or player_1 == "r" and player_2 == "R" or player_2 == "r":
  print("You both picked Rock, draw!")
elif player_1 == "R" or player_1 == "r" and player_2 == "P" or player_2 == "p":
  print("Player1's Rock is smothered by Player2's Paper!")
elif player_1 == "R" or player_1 == "r" and player_2 == "S" or player_2 == "s":
  print("Player1's Rock crushes Player2's Scissors!")
elif player_1 == "P" or player_1 == "p" and player_2 == "R" or player_2 == "r":
  print("Player2's Rock is smothered by Player1's Paper!")
elif player_1 == "P" or player_1 == "p" and player_2 == "P" or player_2 == "p":
  print("You both picked Paper, draw!")
elif player_1 == "P" or player_1 == "p" and player_2 == "S" or player_2 == "s":
  print("Player1's Paper is cut by Player2's Scissors!")
elif player_1 == "S" or player_1 == "s" and player_2 == "R" or player_2 == "r":
  print("Player2's Rock crushes Player1's Scissors!")
elif player_1 == "S" or player_1 == "s" and player_2 == "P" or player_2 == "p":
  print("Player1's Scissors cut Player2's Paper!")
elif player_1 == "S" or player_1 == "s" and player_2 == "S" or player_2 == "s":
  print("You both picked Scissors, draw!")
else:
  print("Invalid move!")