import random
import os

hello = input(
  "Welcome to Cameron's Casino Blackjack, press ENTER to continue!")

name = input("\n\nWhat is your name? ")

money = "100"
fileExists = os.path.exists(name)

if fileExists:
  filehandle = open(name, 'r')
  money = filehandle.read()

amount = int(money)
if amount == 0:
  amount = 100

print("\n\nHow much do you wish to bet?")
print(f"Money: ${amount}\n")
bet = int(input())

if (bet) > (amount):
  print('\nInsuficient Funds, leave the table and try again!\n')
  quit()
if (bet) < 0:
  quit()
else:
  cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  c1 = random.choice(cards)
  c2 = random.choice(cards)
  d1 = random.choice(cards)
  d2 = random.choice(cards)
  dealer = d1 + d2
  total = c1 + c2
  print(f"\n\nYour cards are {c1} and {c2}, score is {total}")
  print(f"\nDealers cards are X and {d2}, score is {d2}\n")

  decision = "H"
  countUser = 0
  runDealer = True
  while decision != "S":
    decision = input("\nType H to hit or S to stand: ")
    if decision == "S":
      print("\n\nStand! \n\n")
    elif decision == "H":
      print("\n\nHit! \n\n")
      countUser = countUser + 1
      if countUser == 1:
        c3 = random.choice(cards)
        total = total + c3
        print(f"Your cards are {c1},{c2} and {c3}, score is {total}\n")
      elif countUser == 2:
        c4 = random.choice(cards)
        total = total + c4
        print(f"Your cards are {c1},{c2},{c3} and {c4}, score is {total}\n")
      else:
        c5 = random.choice(cards)
        total = total + c5
        print(
          f"Your cards are {c1},{c2},{c3},{c4} and {c5}, score is {total}\n")

      if total > 21:
        print("\nThat's a bust, Dealer wins!")
        amount = amount - bet
        runDealer = False
        break
      else:
        if countUser == 3:
          print("\n5-Card Charlie, you win!")
          amount = amount + bet
          runDealer = False
          break
    else:
      print("\n\nPlease enter a valid response! \n")

  if runDealer:
    drawCards = True
    countDealer = 0
    while (drawCards == True):
      if (dealer) >= 15:
        if (dealer) > 21:
          drawCards = False
          print("Dealer busts, you win!\n\n")
          amount = amount + bet
          break
        elif (dealer) > (total):
          drawCards = False
          print("Dealer wins!\n\n")
          amount = amount - bet
          break
        elif (dealer) == (total):
          drawCards = False
          print("Draw, Dealer wins!\n\n")
          amount = amount - bet
          break

      countDealer = countDealer + 1
      if countDealer == 1:
        d3 = random.choice(cards)
        dealer = dealer + d3
      elif countDealer == 2:
        d4 = random.choice(cards)
        dealer = dealer + d4
      else:
        d5 = random.choice(cards)
        dealer = dealer + d5

    if countDealer == 0:
      print(f"Dealers cards are {d1} and {d2} score is {dealer}")
    elif countDealer == 1:
      print(f"Dealers cards are {d1},{d2} and {d3}, score is {dealer}")
    elif countDealer == 2:
      print(f"Dealers cards are {d1},{d2},{d3} and {d4}, score is {dealer}")
    else:
      print(
        f"Dealers cards are {d1},{d2},{d3},{d4} and {d5}, score is {dealer}")
      
  filehandle = open(name, 'w')
  print(f"New Balance: ${amount}")
  filehandle.write(str(amount))
  filehandle.close()