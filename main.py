# Rock Paper Scissors Lizard Spock
import time
import random

results = {1: "ROCK",
           2: "PAPER",
           3: "SCISSORS",
           4: "LIZARD",
           5: "SPOCK"}

print(results)


def test(p1, p2):
    if p1 == p2:
        print("DRAW try again")
    elif ((p1 == 1 and p2 in (3, 4)) or
          (p1 == 2 and p2 in (1, 5)) or
          (p1 == 3 and p2 in (2, 4)) or
          (p1 == 4 and p2 in (2, 5)) or
          (p1 == 5 and p2 in (1, 3))):
        print('WINNER')
    else:
        print("LOSER")
    return;


player1 = input("Enter your name: ")
rounds = input("How may rounds shall we play? ")
print("OK", player1, "best of", rounds, "rounds then")
print("Select 1 for ROCK")
print("Select 2 for PAPER")
print("Select 3 for SCISSORS")
print("Select 4 for LIZARD")
print("Select 5 for SPOCK")

for i in range(3):
    print(3 - i)
    time.sleep(0.5)
    if i == 2:
        print("Go!")

p1_selection = int(input())
p2_selection = random.randint(1, 5)

if p1_selection not in (1, 2, 3, 4, 5):
    print("Choose one of: (1) ROCK , (2) PAPER, (3) SCISSORS, (4) LIZARD or (5) SPOCK")
    p1_selection = input()

test(p1_selection, p2_selection)

print("player1 selected: ", p1_selection)
print("player2 selected: ", p2_selection)
