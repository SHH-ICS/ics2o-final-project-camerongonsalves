import random
money = 100
round = "yes"
round = "Yes"
hello = input(
  "Welcome to Cameron's Casino Blackjack, press ENTER to continue!")
print()
print()
while round == "yes" or round == "Yes":
  cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
  print("How much do you wish to bet?")
  print(f"Money: ${money}")
  print()
  bet = int(input())
  if (bet) > (money):
    print()
    print("Insuficient Funds")
    print()
  if (bet) < (money) or (bet) == (money):
   c1 = random.choice(cards)
   c2 = random.choice(cards)
   d1 = random.choice(cards)
   d2 = random.choice(cards)
   d3 = random.choice(cards)
   d4 = random.choice(cards)
   dealer = d1 + d2
   total = c1 + c2 
   
   print()
   print()
   print(f"Your cards are {c1} and {c2}, score is {total}")
   print()
   print(f"Dealers cards are X and {d2}, score is {d2}")
   print()
   print()
  
   decision = input("Type H to hit or S to stand: ")

   if decision == "S":
     print()
     print()
     print(f"Your cards are {c1} and {c2}, score is {total}")
     print()
     if (dealer)>15 or (dealer) ==15:
       print(f"Dealers cards are {d1} and {d2}, score is {dealer}")
       if (dealer)>(total):
         print()
         print()
         print("Dealer wins!")
       if (total)>(dealer):
         print()
         print()
         print("You win!")
       if (dealer) == (total):
         print()
         print()
         print("Tie, you both get your chips back!")
     if (dealer)<15:
       (dealer) = d1 + d2 + d3
       if (dealer)>15 or (dealer) == 15:
         (dealer) = d1 + d2 + d3
         print(f"Dealers cards are {d1},{d2} and {d3}, score is {dealer}")
         if (dealer)<21 or (dealer) == 21:
           if (dealer)>(total):
             print()
             print()
             print("Dealer wins!")
           if (total)>(dealer):
             print()
             print()
             print("You win!")
           if (dealer) == (total):
             print()
             print()
             print("Tie, you both get your chips back!") 
         if (dealer)>21:
           print()
           print()
           print("Dealer busts, you win!")

   if decision == "H":
     c3 = random.choice(cards)
     total = c1 + c2 + c3
     print()
     print()
     print(f"Your cards are {c1},{c2} and {c3}, score is {total}")
     print()
     if (total)>21:
       print()
       print("That's a bust, Dealer wins!")
     if (total)<21 or (total) ==21:
       print(f"Dealers cards are X and {d2}, score is {d2}")
       print()
       print()
       decision = input("Type H to hit or S to stand: ")

       if decision == "S":
         print()
         print()
         print(f"Your cards are {c1}, {c2} and {c3}, score is {total}")
         print()
         if (dealer)>15 or (dealer) ==15:
           print(f"Dealers cards are {d1} and {d2}, score is {dealer}")
           if (dealer)>(total):
             print()
             print()
             print("Dealer wins!")
           if (total)>(dealer):
             print()
             print()
             print("You win!")
           if (dealer) == (total):
             print()
             print()
             print("Tie, you both get your chips back!")
         if (dealer)<15:
           (dealer) = d1 + d2 + d3
           if (dealer)>15 or (dealer) == 15:
             (dealer) = d1 + d2 + d3
             print(f"Dealers cards are {d1},{d2} and {d3}, score is {dealer}")
             if (dealer)<21 or (dealer) == 21:
               if (dealer)>(total):
                 print()
                 print()
                 print("Dealer wins!")
               if (total)>(dealer):
                 print()
                 print()
                 print("You win!")
               if (dealer) == (total):
                 print()
                 print()
                 print("Tie, you both get your chips back!") 
             if (dealer)>21:
               print()
               print()
               print("Dealer busts, you win!")

       if decision == "H":
         c4 = random.choice(cards)
         total = c1 + c2 + c3 + c4
         print()
         print()
         print(f"Your cards are {c1},{c2},{c2} and {c4}, score is {total}")
         print()
         print(f"Dealers cards are X and {d2}, score is {d2}")
         if (total)>21:
          print("That's a bust, Dealer wins!")
          if (total)<21 or (total) ==21:
            print()
            decision = input("Type H to hit or S to stand ")